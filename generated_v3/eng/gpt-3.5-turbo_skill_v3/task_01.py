from ase import Atoms
from ase.build import bulk

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.5)

# Generate a 2x2x2 supercell
supercell = atoms * (2, 2, 2)

# Print cell info and number of atoms
print("Cell info:")
print("Cell lengths and angles:", atoms.get_cell_lengths_and_angles())
print("\nNumber of atoms:", len(supercell))
