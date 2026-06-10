from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create H2O molecule
atoms = molecule('H2O')

# Set EMT calculator
atoms.calc = EMT()

# Print initial energy
print(f"Energy before optimization: {atoms.get_potential_energy():.4f} eV")

# Optimize using BFGS
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Print final energy
print(f"Energy after optimization: {atoms.get_potential_energy():.4f} eV")
