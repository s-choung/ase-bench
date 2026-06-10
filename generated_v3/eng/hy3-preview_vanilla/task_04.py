from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create H2O molecule
atoms = molecule('H2O')

# Attach EMT calculator
atoms.calc = EMT()

# Print initial energy
print(f"Initial energy: {atoms.get_potential_energy():.4f} eV")

# Optimize geometry
opt = BFGS(atoms)
opt.run(fmax=0.02)

# Print final energy
print(f"Final energy: {atoms.get_potential_energy():.4f} eV")
