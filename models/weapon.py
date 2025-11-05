from models.damage import Damage
from rules.utils import (
    bound_target_value,
    bound_hit_wound_target_value,
    bound_save_target_value,
    roll_test,
    roll_test_with_crit,
)


class Weapon:
    """
    Class representing a weapon in the game.
    Contains every information about the weapon, including its stats and special rules.
    This class handles the main attack resolution process.
    It is used by the Profile class to resolve attacks.
    """

    def __init__(self, weapon_data: dict):
        self.attacks = weapon_data["attacks"]
        self.to_hit = weapon_data["to_hit"]
        self.to_wound = weapon_data["to_wound"]
        self.rend = weapon_data.get("rend", 0)
        self.damage = Damage(weapon_data["damage"])
        self.special_rules = weapon_data.get("special_rules", [])

    def _find_modifier_total_value(self, value_name: int, combat_context: dict) -> int:
        """
        Changes a value depending on both the weapon's special rules and the combat context.
        Returns a relative integer value, without bounds (rules limiting modifiers to +1 or -1).
        """
        value = 0
        weapon_is_companion = any(rule["id"] == "companion" for rule in self.special_rules)
        if not weapon_is_companion:
            for rule in self.special_rules:
                if rule["id"] == f"add_{value_name}" and combat_context.get(rule["condition"]):
                    value += rule["value"]
            value += combat_context.get("add_" + value_name, 0)
        else:
            for rule in self.special_rules:
                if rule["id"] == f"add_{value_name}_companion" and combat_context.get(rule["condition"]):
                    value += rule["value"]
            value += combat_context.get("add_" + value_name + "_companion", 0)

        return value

    def _process_hit_rolls(self, attacks: int, combat_context: dict) -> dict:
        """
        Process the hit rolls based on the weapon's special rules.
        """
        attacks = max(attacks, 1)
        results = {"hits": 0, "wounds": 0, "mortals": 0}
        crit_auto_wound = any(rule["id"] == "crit_auto_wound" for rule in self.special_rules)
        crit_mortal = any(rule["id"] == "crit_mortal" for rule in self.special_rules)
        crit_2_hits = any(rule["id"] == "crit_2_hits" for rule in self.special_rules)
        to_hit_mod = self._find_modifier_total_value("to_hit", combat_context)
        to_hit = bound_hit_wound_target_value(self.to_hit, -to_hit_mod)  # Negative modifier
        # because applied to the target value

        if any([crit_auto_wound, crit_mortal, crit_2_hits]):
            crit_threshold = 5 if any(rule["id"] == "crit_5+" for rule in self.special_rules) else 6
            crit_threshold = 2 if any(rule["id"] == "crit_2+" for rule in self.special_rules) else crit_threshold
            hit_rolls, crit_rolls = roll_test_with_crit(to_hit, attacks, crit_threshold)
            results["hits"] = hit_rolls.sum() - crit_rolls.sum()
            if crit_auto_wound:
                results["wounds"] += crit_rolls.sum()
            if crit_mortal:
                results["mortals"] += crit_rolls.sum()
            if crit_2_hits:
                results["hits"] += crit_rolls.sum()
        else:
            hit_rolls = roll_test(to_hit, attacks)
            results["hits"] = hit_rolls.sum()
        return results

    def _process_wound_rolls(self, hits: int, combat_context: dict) -> dict:
        """
        Process the wound rolls based on the weapon's special rules.
        """
        results = {"wounds": 0}
        to_wound_mod = self._find_modifier_total_value("to_wound", combat_context)
        to_wound = bound_hit_wound_target_value(self.to_wound, -to_wound_mod)
        # Negative modifier because applied to the target value
        results["wounds"] = roll_test(to_wound, hits).sum()

        return results

    def _process_save_rolls(self, wounds: int, enemy_save: int, combat_context: dict) -> dict:
        """
        Processes the save rolls based on the weapon's special rules and
        taking into account the rend of the weapon.
        Any attack where the save roll succeeds is a failed attack.
        Any other attack is a successful attack.
        """
        results = {"successful_attacks": 0}
        save_mod = self._find_modifier_total_value("save", combat_context)
        rend = max(self.rend + self._find_modifier_total_value("rend", combat_context), 0)
        save_mod = save_mod - rend
        save = bound_save_target_value(enemy_save, -save_mod)
        # Negative modifier because applied to the target value
        results["successful_attacks"] = wounds - roll_test(save, wounds).sum()

        return results

    def resolve_attacks(
        self, attack_count: int, enemy_save: int, combat_context: list = None, verbose: bool = False
    ) -> int:
        """
        Attacks with the weapon against a target with a given save.
        The combat_context can include additional information like rerolls, modifiers, etc.
        from either the attacker or the defender.
        """
        if combat_context is None:
            combat_context = []

        results = self._process_hit_rolls(
            attack_count, combat_context
        )  # dic with hits, wounds (crit auto-wounds) and mortals (crit mortals)
        mortals = results["mortals"]  # number of hits that deal mortal wounds
        hits = results["hits"]
        wounds = self._process_wound_rolls(hits, combat_context)["wounds"]  # number of hits that wound
        wounds += results["wounds"]  # add crit auto-wounds to the total wounds
        successful_attacks = self._process_save_rolls(wounds, enemy_save, combat_context)[
            "successful_attacks"
        ]  # remove save rolls from the total wounds

        damage_mod = self._find_modifier_total_value("damage", combat_context)  # get weapon damage modifier

        # Calculate total damage
        total_damage = self.damage.damage_value(samples=successful_attacks + mortals, add_modifier=damage_mod)
        if verbose:
            print("total_damage", total_damage)

        return total_damage
