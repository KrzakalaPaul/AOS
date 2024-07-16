import numpy as np
from profiles import *
from utils import ClipSave
np.set_printoptions(precision=2, suppress=True)

def get_dps(unit):
    saves = np.array([2,3,4,5])
    dps = []
    for save in saves:
        samples = 10000
        dps.append(unit.DPS(save, samples).mean())
    dps = np.array(dps)
    return dps

def get_tankiness_modifier(unit,rend):
    
    health = unit.health*unit.models
    save = unit.save
    if unit.ward is None:
        ward = 7
    else:
        ward = unit.ward
    
    effective_save = save + rend
    effective_save = ClipSave(x = effective_save, x_old = save)
    
    modifier = health / min( (effective_save -1) / 6, 1 )
    modifier = modifier/ min( (ward -1) / 6, 1 ) 

    return modifier


units = [ChaosKnights_Charge(), ChaosKnights_Vanilla(), Varanguard_Charge(), Varanguard_Vanilla(),  
         ChaosLord(), DemonPrince(), Abraxia_Vanilla(), Abraxia_Medium(), Abraxia_All(), Karkadrak_Charge(), Karkadrak_Vanilla(),
         Chosen(), ChaosWarriors(),Ogroids(),
         Warden(),Stoneguard()]

for unit in units:
    print(f'Unit: {unit.name}. Dmg/cost:')
    #print(10*get_dps(unit)/unit.cost)
    print(get_tankiness_modifier(unit,rend=1)*get_dps(unit)/unit.cost)
    #print(get_tankiness_modifier(unit,rend=1))
