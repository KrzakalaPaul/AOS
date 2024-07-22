import numpy as np
from profiles import *
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
         Warden(),Stoneguard(),Eltharion(),Avalenor(), Belakor()]
units = [Windcharger(), Sephireth()]
#units = [Stoneguard(), Stoneguard_11(), Stoneguard_rend1()]

'''
units = [ChaosKnights_Charge(), ChaosKnights_Vanilla(),
        Varanguard_Charge(), Varanguard_Vanilla(), 
        Karkadrak_Charge(), Karkadrak_Vanilla(),
        ChaosLordMounted_Charge(), ChaosLordMounted_Vanilla()]
'''

dps_list = []
name_list = []

for unit in units:
    print(f'Unit: {unit.name}. Dmg/cost:')
    dps = 10*get_dps(unit)/unit.cost
    #print(unit.get_tankiness_modifier(rend=1))
    #dps = unit.get_tankiness_modifier(rend=1)*get_dps(unit)/unit.cost
    print(dps)
    dps_list.append(dps)
    name_list.append(unit.name)

sorted_dps_list, sorted_name_list = zip(*sorted(zip(dps_list, name_list), reverse=True))

print(sorted_name_list)