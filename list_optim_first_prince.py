from LP.utils import Unit, Army

# Define units for Lumineth Realm-lords
# Each unit has an id, cost, value (egal to cost by default), min and max constraints
units = [
    # Heroes
    Unit(id='eternus', cost=180, modifier=0.9, min=0, max=1),
    Unit(id='Spiranx', cost=140, modifier=1.0, min=0, max=1),
    #Unit(id='chaos furies', cost=120, modifier=0.9, min=0, max=1),
    #Unit(id='chaos chariot', cost=90, modifier=0.9, min=0, max=1),
    #Unit(id='Karkadrak', cost=190, modifier=1., min=0, max=1),
    
    # All possible unit for the banner
    Unit(id='knights', cost=250, modifier=1, min=0, max=1),
    Unit(id='knights + leader', cost=250+140, modifier=1.0, min=0, max=1),
    Unit(id='knights x2', cost=500, modifier=0.9, min=0, max=1),
    Unit(id='knights x2 + leader', cost=250*2+140, modifier=1.0, min=0, max=1),
    Unit(id='Chaos Wariors x2', cost=360, modifier=1.0, min=0, max=1),
    Unit(id='Theridons', cost=320, modifier=0.9, min=0, max=1),
    Unit(id='Theridons + Leader', cost=440, modifier=1.0, min=0, max=1),
    
    Unit(id='Abraxia', cost=250, modifier=1.0, min=0, max=1),
    Unit(id='Abraxia Season', cost=300, modifier=1.0, min=1, max=1),
    Unit(id='Demon Prince', cost=250, modifier=0.9, min=0, max=1),
    Unit(id='Varanguard', cost=310, modifier=1.0, min=0, max=1),
]

extra_constraints = [
    {'id_list': ['knights', 
                 'knights + leader', 
                 'knights x2', 
                 'knights x2 + leader',
                 'Chaos Wariors x2',
                 'Theridons',
                 'Theridons + Leader',
                 ], 'min': 0, 'max': 1}, 
    {'id_list': ['Abraxia', 'Abraxia Season'], 'min': 0, 'max': 1},
]

lp = Army(units, extra_constraints, cost_max=580)
lp.solve()