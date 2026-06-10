from ase import Atoms
from ase.build import bulk
from ase.optimize import LBFGS
from ase.calculators.emt import EMT

# Create an Au bulk structure
atoms = bulk('Au', 'fcc', a=3.886)

# Set the EMT calculator
atoms.calc = EMT()

# Optimize the structure
opt = LBFGS(atoms)
opt.run(fmax=0.01)

# Print the results
print(f"Number of optimization steps: {opt.n_steps}")
print(f"Final energy: {atoms.get_potential_energy()}")
