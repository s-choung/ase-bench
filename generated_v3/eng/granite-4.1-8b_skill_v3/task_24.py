from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

# Create Au FCC bulk structure
atoms = bulk('Au', 'fcc')

# Assign EMT calculator
atoms.calc = EMT()

# Optimize using LBFGS
optimizer = LBFGS(atoms)
optimizer.run(fmax=0.01)

# Print the number of optimization steps and final energy
print("Optimization steps taken:", optimizer.get_nsteps())
print("Final energy:", atoms.get_potential_energy())
