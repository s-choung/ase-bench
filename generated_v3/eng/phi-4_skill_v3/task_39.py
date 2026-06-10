from ase.build import bulk
from ase.io import read, write
from ase import atoms

# Define the FCC bulk for gold
bulk_a = bulk('Au', 'fcc', a=4.08)  # 'a' is the lattice constant

# Save the bulk to an XYZ file
write('bulk_a.xyz', bulk_a)

# Read the bulk back from the XYZ file
read_bulk = read('bulk_a.xyz')

# Print the atom types and positions
print('Atom Types:', read_bulk.get_chemical_symbols())
print('Positions:', read_bulk.get_positions())
