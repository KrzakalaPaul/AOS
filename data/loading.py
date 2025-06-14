import json
from pathlib import Path
from models.profile import Profile

def load_faction(faction_name: str) -> dict:
    """Load a faction's units from its JSON file"""
    file_path = Path(__file__).parent / f"../data/factions/{faction_name}.json"
    with open(file_path, "r") as f:
        return json.load(f)


def get_all_units(faction_name=None) -> dict:
    """Load all available units from all faction files or a specific faction if faction_name is provided"""
    units_by_id = {}
    faction_dir = Path(__file__).parent / "../data/factions"

    if faction_name:
        file_paths = [faction_dir / f"{faction_name}.json"]
    else:
        file_paths = faction_dir.glob("*.json")

    for file_path in file_paths:
        with open(file_path, "r") as f:
            faction_data = json.load(f)
            for unit_data in faction_data.get("units", []):
                units_by_id[unit_data["id"]] = unit_data

    return units_by_id

def get_all_profiles(faction_name=None, is_reinforced=False) -> dict:
    all_units_data = get_all_units(faction_name=faction_name)
    all_units = {unit_data["id"]: Profile(unit_data,is_reinforced=is_reinforced) for unit_data in all_units_data.values()}
    return all_units