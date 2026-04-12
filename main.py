from rules.unit_profiles import *
from metrics.unit_metric import *
from metrics.pairwise_metric import *
import numpy as np
from data.loading import get_all_profiles, get_all_units
from models.profile import Profile

np.set_printoptions(precision=2, suppress=True)


def main():
    
    # all_units = get_all_units(faction_name='slaves_to_darkness_new')
    # knights = Profile(all_units["chaos_knights_charge"],is_reinforced=False)
    # fellriders = Profile(all_units["fellriders (SPIKE)"],is_reinforced=True)
    # vaches1 = Profile(all_units["Ogroids Theridons"],is_reinforced=True)
    # vaches2 = Profile(all_units["Ogroids Theridons (SPIKE)"],is_reinforced=True)
    
    # #metric = AlphaStrike(ennemy_unit=varanguard, scale_by_cost=False)
    # #print(average_metric(knights, metric, n_samples=10000))
    # #plot_cdf(knights, metric, n_samples=10000)
    # metrics = [DamageOneActivation(save=s, scale_by_cost=False) for s in [2, 3, 4, 5]]
    # multimetric_plot([knights, vaches1, vaches2, fellriders], metrics, n_samples=1000)
    # metrics = [EffectiveHP(ennemy_rend=s, scale_by_cost=False) for s in [1,2,3,4]]
    # multimetric_plot([knights, vaches1, vaches2, fellriders], metrics, n_samples=1000)
    
    ################ Load all units ################

    # all_profiles = get_all_profiles(faction_name='slaves_to_darkness_new', is_reinforced=True).values()
    # print(f"Loaded {len(all_profiles)} units.")
    # units = all_profiles
    # metrics = [DamageOneActivation(save=s, scale_by_cost=True) for s in [2, 3, 4, 5]]
    # #metrics = [EffectiveHP(ennemy_rend=s, scale_by_cost=True) for s in [1,2,3,4]]
    # multimetric_plot(units, metrics, n_samples=10000)
    # scatter_plot_two_metrics(units, DamageOneActivation(save=3, scale_by_cost=True), EffectiveHP(ennemy_rend=1, scale_by_cost=True), n_samples=5000)

    ################ Print a metric ################
    std_units = get_all_units(faction_name='std_foudoudav')
    archaon = Profile(std_units["Archaon"])
    fec_units = get_all_units(faction_name='fec_boost')
    two_terrorgheist = Profile(fec_units["2 Terrorgheist"])
    three_terrorgheist = Profile(fec_units["3 Terrorgheist"])
    metric = AlphaStrike(ennemy_unit=archaon, scale_by_cost=False, return_n_slain_models=False)
    print('Damage:')
    print(median_metric(two_terrorgheist, metric, n_samples=10000))
    plot_cdf(two_terrorgheist, metric, n_samples=10000)
    print('Proba one shot:')
    archaon = Profile(std_units["Archaon"])
    metric = AlphaStrike(ennemy_unit=archaon, scale_by_cost=False, return_n_slain_models=True)
    print(average_metric(two_terrorgheist, metric, n_samples=10000))
    plot_cdf(two_terrorgheist, metric, n_samples=10000)
    """
    ################ Plot different metrics ################
     
    metrics = [DPS(save=s, scale_by_cost=True) for s in [2, 3, 4, 5]]
    multimetric_plot(units, metrics, n_samples=10000)

    
    ################ Plot different metrics ################
     
    metrics = [DPS(save=s, samples=100, scale_by_cost=True) for s in [2, 3, 4, 5]]
   
    multimetric_plot(units, metrics)
    
    ################ Tournament ################

    metric = winrate(samples=100, initiative=1)

    matrix(units, metric)


    ################ Ranking according to a metric ################

    metric = DPS(save=3, samples=100)

    print(ranking(units, metric))
    """

if __name__ == "__main__":
    main()

"""
import numpy as np
from rules.unit_profiles import *
np.set_printoptions(precision=2, suppress=True)

def get_dps(unit):
    #saves = np.array([2,3,4,5])
    saves = np.array([2,3])
    dps = []
    for save in saves:
        samples = 10000
        dps.append(unit.DPS(save, samples).mean())
    dps = np.array(dps)
    return dps


units = [ChaosKnights_Charge(), ChaosKnights_Vanilla(), Varanguard_Charge(), Varanguard_Vanilla(),  
         ChaosLord(), DemonPrince(), Abraxia_Vanilla(), Abraxia_Medium(), Abraxia_All(), Karkadrak_Charge(), Karkadrak_Vanilla(), 
        ChaosLordMounted_Charge(), ChaosLordMounted_Vanilla(),
         Chosen(), ChaosWarriors(),Ogroids(),ChaosChariot(),
         Warden(),Stoneguard(),Eltharion(),Avalenor(), Belakor(), Slautherbrute()]

#units = [Stoneguard(), Stoneguard_11(), Stoneguard_rend1()]


units = [ChaosKnights_Charge(), ChaosKnights_Vanilla(),
        Varanguard_Charge(), Varanguard_Vanilla(), 
        Karkadrak_Charge(), Karkadrak_Vanilla(),
        ChaosLordMounted_Charge(), ChaosLordMounted_Vanilla()]


dps_list = []
name_list = []

for unit in units:
    print(f'Unit: {unit.name}. Dmg/cost:')
    dps = 10*get_dps(unit)/unit.cost
    #print(unit.get_tankiness_modifier(rend=1))
    dps = unit.get_tankiness_modifier(rend=1)*get_dps(unit)/unit.cost
    print(dps)
    dps_list.append(dps)
    name_list.append(unit.name)

sorted_dps_list, sorted_name_list = zip(*sorted(zip(dps_list, name_list), reverse=True))

print(sorted_name_list)
"""
