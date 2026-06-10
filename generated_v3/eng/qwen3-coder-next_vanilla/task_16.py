from ase import Atoms
from ase.lattice.surface import bcc110

# Create Fe BCC(110) surface with 4 layers, size (2,2,4) and vacuum=10 Å
surface = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

# Print number of atoms and cell size
print(f"Number of atoms: {len(surface)}")
print(f"Cell size: {surface.get_cell()}")
