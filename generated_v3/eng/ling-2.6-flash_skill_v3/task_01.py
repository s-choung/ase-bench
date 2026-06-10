from ase import Atoms
from ase.build import bulk, make_supercell

# Create Cu FCC bulk
cu = bulk('Cu', 'fcc', a=3.6)
# Generate 2x2x2 supercell
supercell = cu * (2, 2, 2)

# Print cell info
print("Cell lengths and angles:", supercell.get_cell_lengths_and_angles())
print("Number of atoms:", len(supercell))
