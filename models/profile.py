from models.weapon import Weapon
from models.abilities import *


class Profile:
    def __init__(self, unit_data: dict, is_reinforced: bool = False):
        self.name = unit_data["name"]
        self.cost = unit_data["point_cost"] if not is_reinforced else unit_data["point_cost"] * 2
        self.total_models = unit_data["model_count"] if not is_reinforced else 2 * unit_data["model_count"]
        self.current_models = unit_data["model_count"] if not is_reinforced else 2 * unit_data["model_count"]
        self.health = unit_data["health"]
        self.save = unit_data["save"]
        self.ward = unit_data.get("ward", None)
        self.champion = unit_data.get("has_champion", True)
        self.wounds_taken = 0
        self.is_destroyed = False

        # Initialize weapons
        self.weapons: list[Weapon] = []
        for weapon_data in unit_data.get("weapons", []):
            weapon = Weapon(weapon_data)
            self.weapons.append(weapon)
        self.abilities = unit_data.get("abilities", [])

    def reset(self):
        """Reset the unit's state for a new simulation."""
        self.current_models = self.total_models
        self.wounds_taken = 0
        self.is_destroyed = False

    def _process_ward_rolls(self, total_damage: int) -> dict:
        """
        Processes the ward rolls based on the weapon's special rules and
        taking into account the enemy's ward save.
        Any damage that goes through the ward removes health from the target.
        Any succeeded ward roll nullifies one damage.
        """
        total_damage -= roll_test(self.ward, total_damage).sum()
        return total_damage

    def attack_with_all_weapons(self, combat_context: dict, enemy_save: int, verbose: bool = False) -> int:
        """Perform attacks with all weapons and return the resulting damage."""
        all_results = []
        for weapon in self.weapons:
            nb_attacks_per_model = weapon.attacks + weapon._find_modifier_total_value(
                value_name="attacks", combat_context=combat_context
            )
            nb_attacks = nb_attacks_per_model * self.current_models
            if self.champion and "companion" not in [rule["id"] for rule in weapon.special_rules]:
                nb_attacks += 1
            results = weapon.resolve_attacks(nb_attacks, enemy_save, combat_context, verbose=verbose)
            all_results.append(results)
        for ability in self.abilities:
            if ability["id"] == "impact_mortals":
                all_results.append(impact_mortals(self.current_models, ability, combat_context))
        return sum(all_results)

    def receive_damage(self, damage: int) -> int:
        """Reduce the unit's health by the damage taken."""
        damage = self._process_ward_rolls(damage) if self.ward else damage
        previous_models = self.current_models
        self.wounds_taken += damage
        models_slain, wounds_taken_model = divmod(self.wounds_taken, self.health)
        self.current_models = max(0, self.total_models - models_slain)
        if self.current_models <= 0:
            self.is_destroyed = True
        killed_models = previous_models - self.current_models
        return damage, killed_models
