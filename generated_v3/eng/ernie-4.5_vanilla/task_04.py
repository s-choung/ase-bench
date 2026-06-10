from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Initialize the H2O molecule
atoms = Atoms('HOH', positions=[[0, 0, 0], [0, 1, 0], [0, 0, 1]])

# Attach the EMT calculator
atoms.calc = EMT()

# Print initial energy
print(f"Initial energy: {atoms.get_potential_energy():.2f} eV")

# Optimize using BFGS
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Print final energy
print(f"Optimized energy: {atoms.get_potential_energy():.2f} eV")
