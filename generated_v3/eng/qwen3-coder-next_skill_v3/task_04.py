from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.build import molecule

# Create water molecule
atoms = molecule('H2O')

# Set EMT calculator
atoms.calc = EMT()

# Print energy before optimization
print(f"Initial energy: {atoms.get_potential_energy():.6f} eV")

# Optimize structure
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Print energy after optimization
print(f"Optimized energy: {atoms.get_potential_energy():.6f} eV")
