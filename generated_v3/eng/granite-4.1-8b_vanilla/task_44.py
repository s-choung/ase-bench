from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

# Create a Cu(111) 4-layer slab
slab = fcc111('Cu', size=(4, 1, 1), vacuum=10.0)

# Tag the bottom 2 layers for fixing
mask = [atom.tag >= 3 for atom in slab]  # Assuming tags start at 1 for top layer

# Apply FixAtoms constraint
constraints = FixAtoms(mask=mask)
slab.constraints = constraints

# Attach EMT calculator
slab.calc = EMT()

# Perform BFGS optimization
opt = BFGS(slab, trajectory=None)
opt.run(fmax=0.05)

# Print original and final coordinates of fixed atoms
print("Original fixed atom positions:")
for atom in slab:
    if atom.tag >= 3:
        print(atom.position)

print("\nOptimized fixed atom positions:")
for atom in opt.get_atoms():
    if atom.tag >= 3:
        print(atom.position)
