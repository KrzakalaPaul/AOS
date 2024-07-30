import numpy as np
from rules.utils import Test, ClipSave, D

def basic_attack(weapon_profile, save, samples):
    '''
    Return dmg (array of lenght samples) against a unit with a given save
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


def complex_attack(weapon_profile, samples):
    '''
    Return:
        - scored = array of size (samples x number of attacks) with 1 if the attack scored a hit
        - dmg = array of size (samples x number of attacks) width the weapon dmg
        - rend = array of size (samples x number of attacks) width the weapon rend
        - mortals = array of size (samples) with the mortals wounds scored
    Use this function when target unit has special rules
    '''
    
    scored = []
    dmg = []
    rend = []
    mortal_dmg = 0
    
    # This loop could be parallelized
    for _ in range(int(weapon_profile['Atk'])):
        
        hits, Crit = Test(weapon_profile['Hit'], 6, samples, return_crits=True)
        wounds = Test(weapon_profile['Wound'], 6, samples)
        
        if weapon_profile['Crit'] == 'Auto-wound':
            wounds = np.logical_or(wounds,Crit)
            
        if weapon_profile['Crit'] == 'Mortal':
            hits = np.logical_and(hits,np.logical_not(Crit))
            mortal_dmg += weapon_profile['Dmg']*Crit
        else:
            mortal_dmg += np.zeros(samples)
        
        scored.append(hits*wounds)
        dmg.append(np.ones(samples) * weapon_profile['Dmg'])
        rend.append(np.ones(samples) * weapon_profile['Rnd'])

        if weapon_profile['Crit'] == '2 Hits':
            
            wounds2 = Test(weapon_profile['Wound'], 6, samples)
            scored.append(Crit*wounds2)
            dmg.append(np.ones(samples) * weapon_profile['Dmg'])
            rend.append(np.ones(samples) * weapon_profile['Rnd'])
        
    scored = np.stack(scored, axis = 1)
    dmg = np.stack(dmg, axis = 1)
    rend = np.stack(rend, axis = 1)
    return scored, dmg, rend, mortal_dmg 
        
        

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
        
    def attack_save(self, save, samples):
        
        dmg = 0
        for weapon in self.weapons:
            unit_weapon = weapon.get_unit_weapon(self.models, self.champion)
            dmg += basic_attack(unit_weapon, save, samples)
            
        return dmg
    
    def attack(self,samples):
        
        scored_all = []
        dmg_all = []
        rend_all = []
        mortal_dmg_all = 0
        
        for weapon in self.weapons:
            unit_weapon = weapon.get_unit_weapon(self.models, self.champion)
            scored, dmg, rend, mortal_dmg  = complex_attack(unit_weapon, samples)
            scored_all.append(scored)
            dmg_all.append(dmg)
            rend_all.append(rend)
            mortal_dmg_all += mortal_dmg.astype(int)

        scored_all = np.concatenate(scored_all, axis = 1)
        dmg_all = np.concatenate(dmg_all, axis = 1)   
        rend_all = np.concatenate(rend_all, axis = 1)
        
        return scored_all, dmg_all, rend_all, mortal_dmg_all
    
    def defend(self, scored, dmg, rend, mortal_dmg):

        effective_save = self.save + rend
        effective_save = ClipSave(x = effective_save, x_old = self.save)
        
        save_roll = D(6, samples = scored.shape)
        pass_save = save_roll < effective_save
        
        dmg = dmg*scored*pass_save
        
        if not(self.ward is None):
            ward_roll = D(6, samples = scored.shape)
            pass_ward = ward_roll < self.ward
            dmg = dmg * pass_ward
            
            ward_roll = D(6, samples = mortal_dmg.shape)
            pass_ward = ward_roll < self.ward
            mortal_dmg = mortal_dmg * pass_ward
            
        dmg = np.sum(dmg, axis = 1) + mortal_dmg
        
        return dmg
    
    def defend_immortal_save(self, scored, dmg, mortal_dmg):
        
        effective_save = self.save 
        
        save_roll = D(6, samples = scored.shape)
        pass_save = save_roll < effective_save
        
        dmg = dmg*scored*pass_save
        
        if not(self.ward is None):
            ward_roll = D(6, samples = scored.shape)
            pass_ward = ward_roll < self.ward
            dmg = dmg * pass_ward
            
            ward_roll = D(6, samples = mortal_dmg.shape)
            pass_ward = ward_roll < self.ward
            mortal_dmg = mortal_dmg * pass_ward
            
        dmg = np.sum(dmg, axis = 1) + mortal_dmg
        
        return dmg

    def get_tankiness_modifier(self,rend):
        #Average number of hits to kill the unit

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
    
    def get_tankiness_modifier_immortal_save(self):
        # Invulnerable save
        
        health = self.health*self.models
        save = self.save
        if self.ward is None:
            ward = 7
        else:
            ward = self.ward
        
        effective_save = save 
        
        modifier = health / min( (effective_save -1) / 6, 1 )
        modifier = modifier/ min( (ward -1) / 6, 1 ) 

        return modifier
