from ortools.linear_solver import pywraplp

class Unit():
    def __init__(self, id, cost, value, min=None, max=None):
        self.id = id
        self.cost = cost
        self.value = value
        self.min = min
        self.max = max
        
class Army():
    def __init__(self, 
                 units,
                 extra_constraints=[],
                 cost_max=2000):
        assert len({u.id for u in units}) == len(units), "Unit ids must be unique"
        self.units = units
        self.cost_max = cost_max
        self.extra_constraints = extra_constraints
        self.init_solver()
        
    def init_solver(self):
        # Init Solver
        self.solver = pywraplp.Solver.CreateSolver("SAT")
        self.infinity = self.solver.infinity()
        # Initialize variables of all units
        for unit in self.units:
            min = unit.min if unit.min is not None else 0.0
            max = unit.max if unit.max is not None else self.infinity
            unit.var = self.solver.IntVar(min, max, unit.id)
        # Constraint on total cost
        total_cost = sum([u.cost * u.var for u in self.units])
        self.solver.Add(total_cost <= self.cost_max)
        # Objective: maximize total value
        objective = sum([u.value * u.var for u in self.units])
        self.solver.Maximize(objective)
        # Add extra constraints
        for constraint in self.extra_constraints:
            self.add_constraint(id_list=constraint['id_list'],
                                min=constraint['min'],
                                max=constraint['max'])        

    def add_constraint(self, id_list, min, max):
        #unit_list = [unit for unit in self.units if unit.id in id_list]
        all_units_id = [unit.id for unit in self.units]
        unit_list = []
        for id in id_list:
            if id in all_units_id:
                unit_list.append(self.units[all_units_id.index(id)])
            else:
                raise ValueError(f"Unit id '{id}' not found in units list.")
        total_count = sum([u.var for u in unit_list])
        self.solver.Add(total_count <= max) if max is not None else self.infinity
        self.solver.Add(total_count >= min) if min is not None else 0.0
        
    def solve(self):
        status = self.solver.Solve()
        ##### Print Solution
        if status == pywraplp.Solver.OPTIMAL:
            print("Solution:")
            print('')
            print("Objective value =", self.solver.Objective().Value())
            print('')
            print("Total cost =", sum([unit.cost * int(unit.var.solution_value()) for unit in self.units]))
            for unit in self.units:
                value = int(unit.var.solution_value())
                id = unit.id
                if value > 0:
                    print(f"{id} x {value} ({unit.cost * value}pts)")
        else:
            print("The problem does not have an optimal solution.")


if __name__ == "__main__":
    # List the units, cost and value
    units = [Unit(id="unit1", cost=1000, value=1),
            Unit(id="unit2", cost=1000, value=2),
            Unit(id="unit3", cost=1000, value=3)]
    
    # Define extra constraints
    extra_constraints = [
                        {'id_list': ['unit1', 'unit2'], 'min': 1, 'max': None}, # At least one of unit1 or unit2
                         ] 

    lp = Army(units, extra_constraints, cost_max=2000)


    lp.solve()

from ortools.linear_solver import pywraplp

class Unit():
    def __init__(self, id, cost, value, min=None, max=None):
        self.id = id
        self.cost = cost
        self.value = value
        self.min = min
        self.max = max
        
class Army():
    def __init__(self, 
                 units,
                 extra_constraints=[],
                 cost_max=2000):
        assert len({u.id for u in units}) == len(units), "Unit ids must be unique"
        self.units = units
        self.cost_max = cost_max
        self.extra_constraints = extra_constraints
        self.init_solver()
        
    def init_solver(self):
        # Init Solver
        self.solver = pywraplp.Solver.CreateSolver("SAT")
        self.infinity = self.solver.infinity()
        # Initialize variables of all units
        for unit in self.units:
            min = unit.min if unit.min is not None else 0.0
            max = unit.max if unit.max is not None else self.infinity
            unit.var = self.solver.IntVar(min, max, unit.id)
        # Constraint on total cost
        total_cost = sum([u.cost * u.var for u in self.units])
        self.solver.Add(total_cost <= self.cost_max)
        # Objective: maximize total value
        objective = sum([u.value * u.var for u in self.units])
        self.solver.Maximize(objective)
        # Add extra constraints
        for constraint in self.extra_constraints:
            self.add_constraint(id_list=constraint['id_list'],
                                min=constraint['min'],
                                max=constraint['max'])        

    def add_constraint(self, id_list, min, max):
        #unit_list = [unit for unit in self.units if unit.id in id_list]
        all_units_id = [unit.id for unit in self.units]
        unit_list = []
        for id in id_list:
            if id in all_units_id:
                unit_list.append(self.units[all_units_id.index(id)])
            else:
                raise ValueError(f"Unit id '{id}' not found in units list.")
        total_count = sum([u.var for u in unit_list])
        self.solver.Add(total_count <= max) if max is not None else self.infinity
        self.solver.Add(total_count >= min) if min is not None else 0.0
        
    def solve(self):
        status = self.solver.Solve()
        ##### Print Solution
        if status == pywraplp.Solver.OPTIMAL:
            print("Solution:")
            print('')
            print("Objective value =", self.solver.Objective().Value())
            print('')
            print("Total cost =", sum([unit.cost * int(unit.var.solution_value()) for unit in self.units]))
            for unit in self.units:
                value = int(unit.var.solution_value())
                id = unit.id
                if value > 0:
                    print(f"{id} x {value} ({unit.cost * value}pts)")
        else:
            print("The problem does not have an optimal solution.")


if __name__ == "__main__":
    # List the units, cost and value
    units = [Unit(id="unit1", cost=1000, value=1),
            Unit(id="unit2", cost=1000, value=2),
            Unit(id="unit3", cost=1000, value=3)]
    
    # Define extra constraints
    extra_constraints = [
                        {'id_list': ['unit1', 'unit2'], 'min': 1, 'max': None}, # At least one of unit1 or unit2
                         ] 

    lp = Army(units, extra_constraints, cost_max=2000)


    lp.solve()

