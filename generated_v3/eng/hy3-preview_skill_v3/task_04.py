from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create H2O molecule
atoms = molecule('H2O')
atoms.calc = EMT()

# Print energy before optimization
print(f"Energy before optimization: {atoms.get_potential_energy():.6f} eV")

# Optimize structure
opt = BFGS(atoms)
opt.run(fmax=0.05)

# Print energy after optimization
print(f"Energy after optimization: {atoms.get_potential_energy():.6f} eV")
