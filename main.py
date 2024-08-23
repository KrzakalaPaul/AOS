from rules.unit_profiles import *
from metrics.unit_metric import multimetric_plot,ranking,DPS
from metrics.pairwise_metric import matrix, winrate
import numpy as np
np.set_printoptions(precision=2, suppress=True)


def main():
    ################ Define Units to study ################

    units = [Eltharion(), Avalenor(), Belakor(), Abraxia_All()]

    ################ Tournament ################

    metric = winrate(samples=10000, initiative = 1)

    matrix(units, metric)

    ################ Plot different metrics ################

    metrics = [DPS(save = s, samples=10000, scale_by_cost=True) for s in [2,3,4,5]]

    multimetric_plot(units, metrics)

    ################ Ranking according to a metric ################

    metric = DPS(save = 3, samples=10000)

    print(ranking(units, metric))


if __name__ == "__main__":
    main()

'''
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
'''