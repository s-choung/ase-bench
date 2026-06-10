from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create H2O molecule
h2o = Atoms('H2O', positions=[[0, 0, 0], [1, 0, 0], [0, 1, 0]])

# Set EMT calculator
h2o.calc = EMT()

# Print initial energy
print("Initial energy:", h2o.get_potential_energy())

# Optimize using BFGS
opt = BFGS(h2o)
opt.run(fmax=0.01)

# Print final energy
print("Final energy:", h2o.get_potential_energy())
