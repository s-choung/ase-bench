from ase import Atoms
from ase.lattice.surface import fcc100

# Create Cu(100) surface with 3 layers, size=(3,3,3), vacuum=12 Å
surface = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)

# Print number of atoms and cell info
print(f"Number of atoms: {len(surface)}")
print(f"Cell vectors:\n{surface.cell}")
