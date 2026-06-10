from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Setup
atoms = molecule('H2O')
atoms.calc = EMT()

# Before optimization
print(f"Initial energy: {atoms.get_potential_energy():.4f} eV")

# Optimization
opt = BFGS(atoms)
opt.run(fmax=0.01)

# After optimization
print(f"Final energy: {atoms.get_potential_energy():.4f} eV")
