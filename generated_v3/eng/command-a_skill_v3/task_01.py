from ase.build import bulk
from ase.build import make_supercell

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)

# Generate 2x2x2 supercell
supercell = make_supercell(atoms, [[2, 0, 0], [0, 2, 0], [0, 0, 2]])

# Print cell info and number of atoms
print("Cell lengths and angles:", supercell.get_cell_lengths_and_angles())
print("Number of atoms:", len(supercell))
