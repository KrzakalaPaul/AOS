from .combat_rules import *
from copy import deepcopy


def update(defender, dmg):
    '''
    Update the defender's models and health after an attack
    '''
    total_health = (defender.models - 1)*defender.health + defender.active_health
    total_health = total_health - dmg
    
    if total_health <= 0:
        defender.models = 0
        defender.active_health = 0
    else:
        defender.models, defender.active_health = divmod(total_health, defender.health)
        if defender.active_health == 0:
            defender.active_health = defender.health
        else:
            defender.models += 1
        

def fight(unit1,unit2, initiative = 'random'):
    
    unit1 = deepcopy(unit1)
    unit2 = deepcopy(unit2)
    
    unit1.active_health = unit1.health
    unit2.active_health = unit2.health
    
    if initiative == 'random':
        initiative = np.random.choice([1,2])
    assert initiative in [1,2], "Invalid value for initiative"
    
    if initiative == 1:
        attacker = unit1
        defender = unit2
    else:
        attacker = unit2
        defender = unit1
        
    turns = 0
    
    while unit1.models > 0 and unit2.models > 0:
        
        turns += 1
        
        scored, dmg, rend, mortal_dmg = attacker.attack(1)
        dmg = defender.defend(scored, dmg, rend, mortal_dmg).item()

        update(defender, dmg)
        
        attacker, defender = defender, attacker
        
    winner = 1 if unit1.models > 0 else 2
    
    log_dic = {'winner': winner, 'turns': turns}
        
    return log_dic

        
        
        
        
        
