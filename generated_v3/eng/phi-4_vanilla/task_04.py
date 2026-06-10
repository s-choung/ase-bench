from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create an H2O molecule
h2o = Atoms('H2O', positions=[[0, 0, 0], [0, 0.76, 0.58], [0, -0.76, 0.58]])

# Attach EMT calculator to the molecule
h2o.set_calculator(EMT())

# Get initial energy
initial_energy = h2o.get_potential_energy()
print(f'Initial Energy: {initial_energy}')

# Optimize the geometry using BFGS
optimizer = BFGS(h2o)
optimizer.run(fmax=0.1)

# Get final energy
final_energy = h2o.get_potential_energy()
print(f'Final Energy: {final_energy}')
