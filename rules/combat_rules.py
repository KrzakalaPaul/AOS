import numpy as np
from rules.utils import Test, ClipSave

def attack(weapon_profile, save, samples):
    '''
    weapon_profile: dict
        Atk: int
            Number of attacks
        Hit: int
            Hit value
        Wound: int
            Wound value
        Dmg: int
            Damage
        Crit: str
            'None', 'Auto-wound', 'Mortal', '2 Hits'
        Rnd: int
            Rend value
    '''
    
    dmg = 0
    for _ in range(weapon_profile['Atk']):
        
        hits, Crit = Test(weapon_profile['Hit'], 6, samples, return_crits=True)
        wounds = Test(weapon_profile['Wound'], 6, samples)
        
        if weapon_profile['Crit'] == 'Auto-wound':
            wounds = np.logical_or(wounds,Crit)
        
        effective_save = save + weapon_profile['Rnd']
        effective_save = ClipSave(x = effective_save, x_old = save)
        
        pass_save = np.logical_not(Test(effective_save, 6, samples))
        
        scored = hits*wounds*pass_save
        
        if weapon_profile['Crit'] == 'Mortal':
            scored = np.logical_or(scored,Crit)
        
        dmg += weapon_profile['Dmg']*scored
        
        if weapon_profile['Crit'] == '2 Hits':
            
            wounds2 = Test(weapon_profile['Wound'], 6, samples)
            pass_save2 = np.logical_not(Test(effective_save, 6, samples))
            scored2 = Crit*wounds2*pass_save2       
            dmg += weapon_profile['Dmg']*scored2
        
    return dmg
        

class Weapon():
    def __init__(self, Atk, Hit, Wound, Rend, Dmg, Crit, Companion):
        self.Atk = Atk
        self.Hit = Hit
        self.Wound = Wound
        self.Rend = Rend
        self.Dmg = Dmg
        assert Crit in [None, 'Auto-wound', 'Mortal', '2 Hits'], "Invalid value for Crit"
        self.Crit = Crit    
        self.Companion = Companion
        
    def get_unit_weapon(self, models, champion):
        unit_weapon = {'Atk': self.Atk*models + (1-self.Companion)*champion, 
                       'Hit': self.Hit, 
                       'Wound': self.Wound, 
                       'Rnd': self.Rend, 
                       'Dmg': self.Dmg,
                       'Crit': self.Crit
                       }
        return unit_weapon

class Profile:
    def __init__(self):
        
        self.name = 'Unit Name'
        self.cost = 250
        
        self.models = 5
        self.health = 4
        self.save = 3
        self.ward = None
        
        weapon1 = Weapon(Atk = 3, Hit = 3, Wound = 3, Rend = -1, Dmg = 1, Crit = None, Companion = False)
        self.weapons = [weapon1]
        
        self.champion = True
        
    def attack(self, save, samples):
        
        dmg = 0
        for weapon in self.weapons:
            unit_weapon = weapon.get_unit_weapon(self.models, self.champion)
            dmg += attack(unit_weapon, save, samples)
            
        return dmg

    def get_tankiness_modifier(self,rend):
        '''
        Average number of hits to kill the unit
        '''
        
        health = self.health*self.models
        save = self.save
        if self.ward is None:
            ward = 7
        else:
            ward = self.ward
        
        effective_save = save + rend
        effective_save = ClipSave(x = effective_save, x_old = save)
        
        modifier = health / min( (effective_save -1) / 6, 1 )
        modifier = modifier/ min( (ward -1) / 6, 1 ) 

        return modifier