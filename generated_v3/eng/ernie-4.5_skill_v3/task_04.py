from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.build import molecule

# Create H2O molecule
atoms = molecule('H2O')

# Set EMT calculator
atoms.calc = EMT()

# Print initial energy
print(f'Initial energy: {atoms.get_potential_energy():.4f} eV')

# Optimize using BFGS
opt = BFGS(atoms)
opt.run(fmax=0.05)

# Print final energy
print(f'Optimized energy: {atoms.get_potential_energy():.4f} eV')
