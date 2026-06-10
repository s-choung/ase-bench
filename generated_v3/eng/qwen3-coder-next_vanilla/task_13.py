from ase import Atoms
from ase.build import bulk
from ase.visualize import view

# Create bulk silicon with diamond structure and lattice constant 5.43 Å
a = 5.43
si_bulk = bulk('Si', 'diamond', a=a)

# Create 3x3x3 supercell
supercell = si_bulk * (3, 3, 3)

# Print number of atoms and cell volume
print(f"Number of atoms: {len(supercell)}")
print(f"Cell volume: {supercell.get_volume():.2f} Å³")
