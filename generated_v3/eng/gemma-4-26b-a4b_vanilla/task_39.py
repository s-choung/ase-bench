from ase.build import bulk
from ase.io import write, read

# Create Au FCC bulk structure
atoms = bulk('Au', 'fcc', a=4.08)

# Save to XYZ format
filename = 'au_bulk.xyz'
write(filename, atoms, format='xyz')

# Read back from file
atoms_read = read(filename)

# Print atom types and positions
print("Atom Types:", atoms_read.get_chemical_symbols())
print("Positions:\n", atoms_read.get_positions())
