from ase.build import fcc111, bulk
from ase.visualize import view

# Create a bulk silicon structure with diamond lattice
si_bulk = bulk('Si', 'diamond', a=5.43)

# Create a 3x3x3 supercell
si_supercell = si_bulk.repeat((3, 3, 3))

# Print the number of atoms and cell volume
print(f"Number of atoms: {len(si_supercell)}")
print(f"Cell volume: {si_supercell.get_volume()} Å³")
