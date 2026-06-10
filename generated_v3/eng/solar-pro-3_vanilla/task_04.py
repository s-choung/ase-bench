from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

# initial H2O geometry (H-O-H angle ≈ 105°)
water = Atoms('H2O',
             positions=[[0, 0, -0.1],   # H left
                       [0, 0, 0.0],    # O
                       [0, 0, 0.1]],   # H right
             cell=(10, 10, 10),
             pbc=False)

# EMT calculator
calc = EMT()
water.set_calculator(calc)

# print initial energy
print(f'Initial energy: {water.get_potential_energy():.6f}')

# BFGS optimization
dyn = BFGS(water)
dyn.run(fmax=0.01)

# print final energy
print(f'Final energy: {water.get_potential_energy():.6f}')
