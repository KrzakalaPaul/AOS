from LP.utils import Unit, Army

# Define units for Lumineth Realm-lords
# Each unit has an id, cost, value (egal to cost by default), min and max constraints
units = [
    # Heroes
    Unit(id='abraxia, spear of the everchosen', cost=250, modifier=1., min=0, max=1),  # standard profile
    Unit(id='be’lakor, the dark master', cost=450, modifier=1.0, min=0, max=1),
    Unit(id='chaos sorcerer lord', cost=120, modifier=1., min=0, max=1),
    Unit(id='scourge of ghyran – abraxia, spear of the everchosen', cost=300, modifier=1.0, min=0, max=1),  
    Unit(id='Archaon healing pack', cost=810+120+20+10, modifier=1.0, min=0, max=1),  

    # Units
    Unit(id='mindstealer', cost=140, modifier=1.0, min=0, max=1),
    Unit(id='Theridons', cost=320, modifier=1.0, min=0, max=1),
    Unit(id='Theridons + ogroid myrmidon', cost=440, modifier=1.0, min=0, max=1),
    Unit(id='Varangard', cost=310, modifier=1.1, min=0, max=2),
    Unit(id='chaos chariot', cost=90, modifier=0.9, min=0, max=1),
    Unit(id='chaos chosen', cost=540, modifier=1., min=0, max=1),
    Unit(id='chaos furies', cost=120, modifier=0.9, min=0, max=1),
    Unit(id='chaos knights', cost=250, modifier=1., min=0, max=1),
    Unit(id='chaos knights x2', cost=500, modifier=1., min=0, max=1),
    Unit(id='chaos warriors', cost=360, modifier=1., min=0, max=1),
    Unit(id='raptoryx', cost=100, modifier=0.9, min=0, max=1),
    # Spell Lore
    # Unit(id='lore', cost=20, modifier=1, min=0, max=1),
]

extra_constraints = [
    {'id_list': ['be’lakor, the dark master', 'chaos sorcerer lord'], 'min': None, 'max': 2},  # Max number of casters
    {'id_list': ['Theridons', 'Theridons + ogroid myrmidon'], 'min': None, 'max': 1},  # Max number of Theridons
    {'id_list': ['chaos knights', 'chaos knights x2'], 'min': None, 'max': 1},  # Max number of Chaos Knights
    {'id_list': ['chaos chariot', 'chaos furies', 'raptoryx'], 'min': None, 'max': 1},  # Max number of screen units
    {'id_list': ['abraxia, spear of the everchosen', 'scourge of ghyran – abraxia, spear of the everchosen'], 'min': 0, 'max': 1},  # Max number of Abraxia
]

lp = Army(units, extra_constraints, cost_max=2000)
lp.add_noise(noise_factor=0.1)  # Add noise to unit values to break ties
lp.solve()