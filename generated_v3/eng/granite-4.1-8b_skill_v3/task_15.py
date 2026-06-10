from ase import Atoms
from ase.build import fcc100

# Build Cu(100) surface with 3 layers, size=(3,3,3) and 12 Å vacuum
slab = fcc100('Cu', size=(3, 3, 3), vacuum=12)

# Print number of atoms and cell information
print(f"Number of atoms: {len(slab)}")
print("Cell vectors (Å):")
print(slab.cell)
