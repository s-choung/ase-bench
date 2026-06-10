from ase.build import bulk
from ase import Atoms

# Create Si bulk with diamond structure and a lattice constant of 5.43 angstroms
si_bulk = bulk('Si', 'diamond', a=5.43)

# Generate a 3x3x3 supercell
supercell_si = si_bulk.repeat((3, 3, 3))

# Print the number of atoms and the cell volume
print('Number of atoms:', len(supercell_si))
print('Cell volume:', supercell_si.get_volume())
