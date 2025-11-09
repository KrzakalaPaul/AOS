from LP.utils import Unit, Army

# Define units for Lumineth Realm-lords
# Each unit has an id, cost, value (egal to cost by default), min and max constraints
units = [
    # Base units
    Unit(id='bladelords', cost=300, value=300*1.05, min=None, max=1),
    Unit(id='riverblades', cost=160, value=160, min=None, max=1),
    Unit(id='wardens', cost=280, value=280*1.20, min=None, max=1),
    Unit(id='sentinels', cost=320, value=320*0.8, min=None, max=1),
    Unit(id='dawnriders', cost=440, value=440*1.1, min=None, max=1),
    Unit(id='dawnriders (simple)', cost=220, value=220*1.1, min=None, max=1),
    Unit(id='stoneguard', cost=240, value=240*1.05, min=None, max=1),
    # Heroes
    Unit(id='eltharion scourge', cost=270, value=270*0.9, min=None, max=1),
    Unit(id='eltharion', cost=210, value=210*0.9, min=None, max=1),
    Unit(id='lord regent', cost=210, value=210*1.0, min=None, max=1),
    Unit(id='enlightener', cost=180, value=180*1.1, min=None, max=1),
    # Combinations (for synergies)
    Unit(id='stoneguard + stonemage', cost=360, value=360*1.1, min=None, max=1),
     Unit(id='stoneguard + stonemage + Avalenor', cost=770, value=770*0.95, min=None, max=1),
    # Special
    Unit(id='silver wand', cost=20, value=60, min=None, max=1),
    Unit(id='shrine', cost=20, value=60, min=None, max=1),
]

# Define extra constraints here
# e.g. "at least one of eltharion or eltharion scourge" and "at most one of eltharion or eltharion scourge"
extra_constraints = [
                    {'id_list': ['eltharion scourge', 'eltharion'], 'min': None, 'max': 1},  # Max one type of Eltharion
                    {'id_list': ['lord regent', 'eltharion scourge', 'eltharion'], 'min': 1, 'max': None},  # At least one leader for dawnriders
                    {'id_list': ['enlightener', 'enlightener', 'stoneguard + stonemage', 'lord regent', 'silver wand'], 'min': 3, 'max': 5},  # Between 3 and 5 caster
                    {'id_list': ['stoneguard + stonemage', 'stoneguard',"stoneguard + stonemage + Avalenor"], 'min': 0, 'max': 1},  
                        ] 

lp = Army(units, extra_constraints, cost_max=2000)
lp.solve()