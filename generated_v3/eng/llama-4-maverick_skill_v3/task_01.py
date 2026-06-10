from ase import Atoms
from ase.build import bulk, make_supercell

# Create Cu FCC bulk
cu_bulk = bulk('Cu', 'fcc', a=3.6)

# Generate 2x2x2 supercell
P = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]
cu_supercell = make_supercell(cu_bulk, P)

# Print cell info and number of atoms
print(f"Cell lengths and angles: {cu_supercell.get_cell_lengths_and_angles()}")
print(f"Number of atoms: {len(cu_supercell)}")
