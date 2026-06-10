from ase.build import bulk
from ase.io import write, read

# Create Au FCC bulk
atoms = bulk('Au', 'fcc', a=4.08)

# Save to XYZ format
write('au_bulk.xyz', atoms)

# Read back from XYZ
atoms_read = read('au_bulk.xyz')

# Print atom types and positions
print("Atom types:", atoms_read.get_chemical_symbols())
print("Positions:\n", atoms_read.get_positions())
