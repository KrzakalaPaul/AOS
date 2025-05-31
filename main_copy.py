from fastapi import FastAPI

from rules.unit_profiles import *
from metrics.unit_metric import *
from metrics.pairwise_metric import *
import numpy as np
from data.loading import get_all_profiles, get_all_units
from models.profile import Profile

np.set_printoptions(precision=2, suppress=True)

app = FastAPI()


def test_fight():
    ################ Load all units ################

    all_units = get_all_units()
    knights = Profile(all_units["chaos_knights_charge"], is_reinforced=True)
    dawnriders = Profile(all_units["Vanari_Dawnriders_charge"], is_reinforced=True)

    ################ Print a metric ################

    metric = AlphaStrike(ennemy_unit=knights, scale_by_cost=False)
    # metric = DPS(save=4, scale_by_cost=False)
    # metric = AlphaStrike(ennemy_unit=knights, scale_by_cost=False)
    # print(average_metric(units[1], metric, n_samples=10000))
    multi_unit_plot_cdf([knights, dawnriders], metric, n_samples=10000)


@app.get("/profiles/{profile_name}")
async def get_profile(profile_name: str):
    """
    Endpoint to retrieve a specific unit profile by name.
    """
    all_units = get_all_units()
    if profile_name in all_units:
        return all_units[profile_name]
    else:
        return {"error": "Profile not found"}


@app.get("/profiles/{profile_name}/weapons")
async def get_profile_weapon(profile_name: str, weapon_id: int = 0):
    """
    Endpoint to retrieve a specific weapon from a unit profile by name and weapon ID.
    """
    all_units = get_all_units()
    if profile_name in all_units:
        unit = all_units[profile_name]
        if "weapons" in unit and len(unit["weapons"]) > weapon_id:
            return unit["weapons"][weapon_id]
        else:
            return {"error": "Weapon not found"}
    else:
        return {"error": "Profile not found"}


@app.get("/")
async def root():
    return {"message": "Welcome to the Warhammer AOS API!"}
