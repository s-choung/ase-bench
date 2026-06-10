from ase.build import fcc111
from ase import Atoms

# Create Cu(100) surface with 3 layers and add vacuum
surface = fcc111('Cu', size=(3, 3, 3), vacuum=12)

# Print the number of atoms and cell information
print(f"Number of atoms: {len(surface)}")
print("Cell information:")
print(surface.cell)
