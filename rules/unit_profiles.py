from .combat_rules import *
from .utils import miniD3

class ChaosKnights_Charge(Profile):
    def __init__(self):
        
        self.name = 'Chaos Knights (Charge)'
        self.cost = 250
        
        self.models = 5
        self.health = 4
        self.save = 3
        self.ward = None
        
        weapon1 = Weapon(Atk = 3, Hit = 3, Wound = 3, Rend = 2, Dmg = 2, Crit = None, Companion = False)
        weapon2 = Weapon(Atk = 2, Hit = 5, Wound = 3, Rend = 0, Dmg = 2, Crit = None, Companion = True)
        self.weapons = [weapon1, weapon2]
        
        self.champion = True
        
class ChaosKnights_Vanilla(Profile):
    def __init__(self):
        
        self.name = 'Chaos Knights (Vanilla)'
        self.cost = 250
        
        self.models = 5
        self.health = 4
        self.save = 3
        self.ward = None
        
        weapon1 = Weapon(Atk = 3, Hit = 3, Wound = 3, Rend = 1, Dmg = 1, Crit = None, Companion = False)
        weapon2 = Weapon(Atk = 2, Hit = 5, Wound = 3, Rend = 0, Dmg = 2, Crit = None, Companion = True)
        self.weapons = [weapon1, weapon2]
        
        self.champion = True
        
class Varanguard_Vanilla(Profile):
    def __init__(self):
        
        self.name = 'Varanguard (Vanilla)'
        self.cost = 310
        
        self.models = 3
        self.health = 5
        self.save = 3
        self.ward = None
        
        weapon1 = Weapon(Atk = 3, Hit = 3, Wound = 3, Rend = 2, Dmg = 2, Crit = 'Mortal', Companion = False)
        weapon2 = Weapon(Atk = 3, Hit = 4, Wound = 3, Rend = 1, Dmg = 1, Crit = None, Companion = True)
        self.weapons = [weapon1, weapon2]
        
        self.champion = False
        
class Varanguard_Charge(Profile):
    def __init__(self):
        
        self.name = 'Varanguard (Charge)'
        self.cost = 310
        
        self.models = 3
        self.health = 5
        self.save = 3
        self.ward = None
        
        weapon1 = Weapon(Atk = 3, Hit = 3, Wound = 3, Rend = 2, Dmg = 3, Crit = 'Mortal', Companion = False)
        weapon2 = Weapon(Atk = 3, Hit = 4, Wound = 3, Rend = 1, Dmg = 1, Crit = None, Companion = True)
        self.weapons = [weapon1, weapon2]
        
        self.champion = False
        

class ChaosLord(Profile):
    def __init__(self):
        
        self.name = 'Chaos Lord'
        self.cost = 140
        
        self.models = 1
        self.health = 6
        self.save = 3
        self.ward = None
        
        weapon1 = Weapon(Atk = 5, Hit = 3, Wound = 3, Rend = 1, Dmg = 2, Crit = 'Mortal', Companion = False)
        self.weapons = [weapon1]
        
        self.champion = False
        

class DemonPrince(Profile):
    def __init__(self):
        
        self.name = 'Demon Prince'
        self.cost = 280
        
        self.models = 1
        self.health = 10
        self.save = 3
        self.ward = 6
        
        weapon1 = Weapon(Atk = 6, Hit = 3, Wound = 3, Rend = 1, Dmg = 3, Crit = 'Mortal', Companion = False)
        self.weapons = [weapon1]
        
        self.champion = False
        
        
class Abraxia_Vanilla(Profile):
    def __init__(self):
        
        self.name = 'Abraxia (Vanilla)'
        self.cost = 360
        
        self.models = 1
        self.health = 14
        self.save = 3
        self.ward = 5
        
        weapon1 = Weapon(Atk = 5, Hit = 3, Wound = 3, Rend = 2, Dmg = 2, Crit = None, Companion = False)
        weapon2 = Weapon(Atk = 6, Hit = 4, Wound = 3, Rend = 1, Dmg = 2, Crit = None, Companion = False)
        self.weapons = [weapon1, weapon2]
        
        self.champion = False
        
class Abraxia_Medium(Profile):   
    def __init__(self):
        
        self.name = 'Abraxia (Anti Hero + 3+)'
        self.cost = 360
        
        self.models = 1
        self.health = 14
        self.save = 3
        self.ward = 5
        
        weapon1 = Weapon(Atk = 5, Hit = 3, Wound = 3, Rend = 3, Dmg = 3, Crit = None, Companion = False)
        weapon2 = Weapon(Atk = 6, Hit = 4, Wound = 3, Rend = 1, Dmg = 2, Crit = None, Companion = False)
        self.weapons = [weapon1, weapon2]
        
        self.champion = False
     
class Abraxia_All(Profile):
    def __init__(self):
        
        self.name = 'Abraxia (Charge + Anti Hero + 6)'
        self.cost = 360
        
        self.models = 1
        self.health = 14
        self.save = 3
        self.ward = 5
        
        weapon1 = Weapon(Atk = 5, Hit = 3, Wound = 3, Rend = 3, Dmg = 4, Crit = 'Mortal', Companion = False)
        weapon2 = Weapon(Atk = 6, Hit = 4, Wound = 3, Rend = 1, Dmg = 2, Crit = None, Companion = False)
        self.weapons = [weapon1, weapon2]
        
        self.champion = False
        
class Karkadrak_Vanilla(Profile):
    def __init__(self):
        
        self.name = 'Karkadrak (Vanilla)'
        self.cost = 250
        
        self.models = 1
        self.health = 10
        self.save = 3
        self.ward = None
        
        weapon1 = Weapon(Atk = 5, Hit = 3, Wound = 3, Rend = 1, Dmg = 2, Crit = 'Mortal', Companion = False)
        weapon2 = Weapon(Atk = 4, Hit = 4, Wound = 3, Rend = 1, Dmg = 2, Crit = None, Companion = False)
        self.weapons = [weapon1, weapon2]
        
        self.champion = False
        
class Karkadrak_Charge(Profile):
    def __init__(self):
        
        self.name = 'Karkadrak (Charge)'
        self.cost = 250
        
        self.models = 1
        self.health = 10
        self.save = 3
        self.ward = None
        
        weapon1 = Weapon(Atk = 5, Hit = 3, Wound = 3, Rend = 1, Dmg = 3, Crit = 'Mortal', Companion = False)
        weapon2 = Weapon(Atk = 4, Hit = 4, Wound = 3, Rend = 1, Dmg = 2, Crit = None, Companion = False)
        self.weapons = [weapon1, weapon2]
        
        self.champion = False
    
    def attack_save(self, save, samples):
        dmg = super(Karkadrak_Charge,self).attack_save(save, samples)
        # add dmg from charge 
        dmg += miniD3(samples)
        
        return dmg
    
    def attack(self, samples):
        scored_all, dmg_all, rend_all, mortal_dmg_all = super(Karkadrak_Charge,self).attack(samples)
        # add dmg from charge 
        mortal_dmg_all += miniD3(samples)
        
        return scored_all, dmg_all, rend_all, mortal_dmg_all
        
        
class Chosen(Profile):
    
    def __init__(self):
        
        self.name = 'Chosen'
        self.cost = 250
        
        self.models = 5
        self.health = 3
        self.save = 3
        self.ward = None
        
        weapon1 = Weapon(Atk = 3, Hit = 3, Wound = 3, Rend = 1, Dmg = 2, Crit = 'Mortal', Companion = False)
        self.weapons = [weapon1]
        
        self.champion = True
        
class ChaosWarriors(Profile):
    
    def __init__(self):
        
        self.name = 'Chaos Warriors'
        self.cost = 200
        
        self.models = 10
        self.health = 2
        self.save = 3
        self.ward = None
        
        weapon1 = Weapon(Atk = 2, Hit = 3, Wound = 3, Rend = 1, Dmg = 1, Crit = None, Companion = False)
        self.weapons = [weapon1]
        
        self.champion = True
        
class Ogroids(Profile):
    
    def __init__(self):
        
        self.name = 'Ogroid (Anti Infantery + OncePerBattle)'
        self.cost = 200
        
        self.models = 3
        self.health = 5
        self.save = 4
        self.ward = None
        
        weapon1 = Weapon(Atk = 4, Hit = 4, Wound = 2, Rend = 2, Dmg = 3, Crit = None, Companion = False)
        self.weapons = [weapon1]
        
        self.champion = True
        
class ChaosChariot(Profile):
    
    def __init__(self):
        
        self.name = 'Chaos Chariot'
        self.cost = 110
        
        self.models = 1
        self.health = 7
        self.save = 4
        self.ward = None
        
        weapon1 = Weapon(Atk = 6, Hit = 3, Wound = 3, Rend = 0, Dmg = 1, Crit = None, Companion = False)
        weapon2 = Weapon(Atk = 2, Hit = 4, Wound = 4, Rend = 0, Dmg = 1, Crit = None, Companion = False)
        weapon3 = Weapon(Atk = 4, Hit = 5, Wound = 3, Rend = 0, Dmg = 1, Crit = None, Companion = True)
        self.weapons = [weapon1,weapon2,weapon3]
        
        self.champion = False
    
    def attack_save(self, save, samples):
        dmg = super(ChaosChariot,self).attack_save(save, samples)
        # add dmg from charge 
        dmg += miniD3(samples)
        
        return dmg
    
    def attack(self, samples):
        scored_all, dmg_all, rend_all, mortal_dmg_all = super(ChaosChariot,self).attack(samples)
        # add dmg from charge 
        mortal_dmg_all += miniD3(samples)
        
        return scored_all, dmg_all, rend_all, mortal_dmg_all
        
class ChaosLordMounted_Vanilla(Profile):
    
    def __init__(self):
        
        self.name = 'Mounted Chaos Lord (Vanilla)'
        self.cost = 180
        
        self.models = 1
        self.health = 8
        self.save = 3
        self.ward = None
        
        weapon1 = Weapon(Atk = 5, Hit = 3, Wound = 3, Rend = 2, Dmg = 2, Crit = None, Companion = False)
        weapon2 = Weapon(Atk = 3, Hit = 5, Wound = 3, Rend = 0, Dmg = 1, Crit = None, Companion = True)
        
        self.weapons = [weapon1,weapon2]
        
        self.champion = False
         
class ChaosLordMounted_Charge(Profile):
    
    def __init__(self):
        
        self.name = 'Mounted Chaos Lord (Charge)'
        self.cost = 180
        
        self.models = 1
        self.health = 8
        self.save = 3
        self.ward = None
        
        weapon1 = Weapon(Atk = 5, Hit = 3, Wound = 3, Rend = 2, Dmg = 3, Crit = None, Companion = False)
        weapon2 = Weapon(Atk = 3, Hit = 5, Wound = 3, Rend = 0, Dmg = 1, Crit = None, Companion = True)
        
        self.weapons = [weapon1,weapon2]
        
        self.champion = False
        
class Belakor(Profile):
    def __init__(self):
        
        self.name = "Be'Lakor"
        self.cost = 410 - 200
        
        self.models = 1
        self.health = 14
        self.save = 4
        self.ward = 6
        
        weapon1 = Weapon(Atk = 8, Hit = 3, Wound = 3, Rend = 2, Dmg = 2, Crit = 'Auto-wound', Companion = False)
        weapon2 = Weapon(Atk = 2, Hit = 2, Wound = 2, Rend = 2, Dmg = 3, Crit = None, Companion = False)
        
        self.weapons = [weapon1,weapon2]
        
        self.champion = False
        
    def get_tankiness_modifier(self,rend):
        return self.get_tankiness_modifier_immortal_save()
    
    def defend(self,scored, dmg, rend, mortal_dmg):
        return self.defend_immortal_save(scored, dmg, mortal_dmg)
        
class Slautherbrute(Profile):
    
    def __init__(self):
        
        self.name = 'Slaughterbrute (charging infantery with all out attack)'
        self.cost = 240

        self.models = 1
        self.health = 14
        self.save = 4
        self.ward = None
        
        weapon1 = Weapon(Atk=8, Hit=3, Wound=2, Rend=2, Dmg=2, Companion = True, Crit = None)
        weapon2 = Weapon(Atk=2, Hit=3, Wound=2, Rend=1, Dmg=3, Companion = True, Crit = None)
        
        self.weapons = [weapon1,weapon2]
        
        self.champion = False
    
    def attack_save(self, save, samples):
        dmg = super(Slautherbrute,self).attack_save(save, samples)
        # add dmg from charge 
        dmg += 2*miniD3(samples)
        
        return dmg
    
    def attack(self, samples):
        scored_all, dmg_all, rend_all, mortal_dmg_all = super(Slautherbrute,self).attack(samples)
        # add dmg from charge 
        mortal_dmg_all += 2*miniD3(samples)
        
        return scored_all, dmg_all, rend_all, mortal_dmg_all
        

class Warden(Profile):
    
    def __init__(self):
        
        self.name = 'Warden'
        self.cost = 150
        
        self.models = 10
        self.health = 1
        self.save = 4
        self.ward = None
        
        weapon1 = Weapon(Atk = 2, Hit = 3, Wound = 4, Rend = 1, Dmg = 1, Crit = 'Mortal', Companion = False)
        self.weapons = [weapon1]
        
        self.champion = True
        
class Stoneguard(Profile):
    
    def __init__(self):
        
        self.name = 'Stoneguard buffed'
        self.cost = 130
        
        self.models = 5
        self.health = 2
        self.save = 4
        self.ward = 5
        
        weapon1 = Weapon(Atk = 3, Hit = 3, Wound = 3, Rend = 2, Dmg = 2, Crit = None, Companion = False)
        self.weapons = [weapon1]
        
        self.champion = True
        
    def get_tankiness_modifier(self,rend):
        rend = max(rend - 1,0)
        return super(Stoneguard,self).get_tankiness_modifier(rend)
    
    def defend(self,scored, dmg, rend, mortal_dmg):
        rend = np.maximum(rend - 1,0)
        return super(Stoneguard,self).defend(scored, dmg, rend, mortal_dmg)
        
        
class Eltharion(Profile):
    
    def __init__(self):
        
        self.name = 'Eltharion'
        self.cost = 250
        
        self.models = 1
        self.health = 6
        self.save = 3
        self.ward = 5
        
        weapon1 = Weapon(Atk = 4, Hit = 2, Wound = 3, Rend = 3, Dmg = 3, Crit = '2 Hits', Companion = False)
        weapon2 = Weapon(Atk = 2, Hit = 2, Wound = 3, Rend = 2, Dmg = 3, Crit = None, Companion = False)
        self.weapons = [weapon1,weapon2]
        
        self.champion = False
        
    def get_tankiness_modifier(self,rend):
        return self.get_tankiness_modifier_immortal_save()
    
    def defend(self,scored, dmg, rend, mortal_dmg):
        return self.defend_immortal_save(scored, dmg, mortal_dmg)
    
    
class Windcharger(Profile):
    
    def __init__(self):
        
        self.name = 'Windcharger'
        self.cost = 170
        
        self.models = 5
        self.health = 3
        self.save = 4
        self.ward = None
        
        weapon1 = Weapon(Atk = 3, Hit = 3, Wound = 4, Rend = 1, Dmg = 1, Crit = None, Companion = False)
        self.weapons = [weapon1]
        
        self.champion = True

class Sephireth(Profile):
    
    def __init__(self):
        
        self.name = 'Sephireth'
        self.cost = 360
        
        self.models = 1
        self.health = 10
        self.save = 4
        self.ward = None
        
        weapon1 = Weapon(Atk = 4, Hit = 2, Wound = 3, Rend = 3, Dmg = 3, Crit = None, Companion = False)
        self.weapons = [weapon1]
        
        self.champion = True
        
    
class Avalenor(Profile):
    
    def __init__(self):
    
        self.name = 'Avalenor'
        self.cost = 410
        
        self.models = 1
        self.health = 16
        self.save = 3
        self.ward = 6
        
        weapon1 = Weapon(Atk = 6, Hit = 3, Wound = 2, Rend = 2, Dmg = 4, Crit = None, Companion = False)
        weapon2 = Weapon(Atk = 2, Hit = 4, Wound = 2, Rend = 1, Dmg = 2, Crit = None, Companion = False)
        self.weapons = [weapon1,weapon2]
        
        self.champion = False
    
    def get_tankiness_modifier(self,rend):
        rend = max(rend - 2,0)
        return super(Avalenor,self).get_tankiness_modifier(rend)
    
    def defend(self,scored, dmg, rend, mortal_dmg):
        rend = np.maximum(rend - 2,0)
        return super(Avalenor,self).defend(scored, dmg, rend, mortal_dmg)