import math
from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

bond_length = 0.96
bond_angle = math.radians(104.5)
positions = [
    [0, 0, 0],
    [bond_length, 0, 0],
    [bond_length * math.cos(bond_angle), bond_length * math.sin(bond_angle), 0]
]
h2o = Atoms(['O', 'H', 'H'], positions=positions)
h2o.set_calculator(EMT())
print("Initial energy:", h2o.get_potential_energy())
BFGS(h2o).run(fmax=0.01)
print("Final energy:", h2o.get_potential_energy())
