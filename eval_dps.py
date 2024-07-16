import numpy as np
from utils import Test, ClipSave


def DPS(profile, save, samples):
    
    dmg = 0
    for _ in range(profile['Atk']):
        
        hits, Crit = Test(profile['Hit'], 6, samples, return_crits=True)
        wounds = Test(profile['Wound'], 6, samples)
        
        if profile['Crit'] == 'Auto-wound':
            wounds = np.logical_or(wounds,Crit)
        
        effective_save = save + profile['Rnd']
        effective_save = ClipSave(x = effective_save, x_old = save)
        
        pass_save = np.logical_not(Test(effective_save, 6, samples))
        
        scored = hits*wounds*pass_save
        
        if profile['Crit'] == 'Mortal':
            scored = np.logical_or(scored,Crit)
        
        dmg += profile['Dmg']*scored
        
        if profile['Crit'] == '2 Hits':
            
            wounds2 = Test(profile['Wound'], 6, samples)
            pass_save2 = np.logical_not(Test(effective_save, 6, samples))
            scored2 = Crit*wounds2*pass_save2       
            dmg += profile['Dmg']*scored2
        
    return dmg
        
        
        
          
