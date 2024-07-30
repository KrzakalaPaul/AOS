
from rules.combat_rules import Profile, Weapon
from rules.fight import fight

class Attaquant(Profile):
    def __init__(self):
        
        self.name = 'Attaquant'
        self.cost = 250
        
        self.models = 1
        self.health = 1
        self.save = 3
        self.ward = None
        
        weapon = Weapon(Atk = 1, Hit = 0, Wound = 0, Rend = 0, Dmg = 1, Crit = None, Companion = False)
        self.weapons = [weapon]
        
        self.champion = False
        
class Defenseur(Profile):
    def __init__(self):
        
        self.name = 'Defenseur'
        self.cost = 250
        
        self.models = 1
        self.health = 1
        self.save = 7
        self.ward = None
        
        weapon = Weapon(Atk = 1, Hit = 0, Wound = 0, Rend = 0, Dmg = 0, Crit = None, Companion = False)
        self.weapons = [weapon]
        
        self.champion = False
        
        

unit1 = Attaquant()
unit2 = Defenseur()
log_dic = fight(unit1,unit2, initiative = 1)
print(log_dic)


'''
scored, dmg, rend, mortal_dmg = Attaquant().attack(5)
dmg = Defenseur().defend(scored, dmg, rend, mortal_dmg)

print(dmg)
'''