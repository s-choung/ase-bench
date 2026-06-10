from ase.build import bulk
from ase.io import write, read

# Create Au FCC bulk
atoms = bulk('Au', 'fcc', a=4.08)

# Save to XYZ format
write('structure.xyz', atoms, format='xyz')

# Read back from XYZ
atoms_read = read('structure.xyz', format='xyz')

# Print atom types and positions
print("Symbols:", atoms_read.get_chemical_symbols())
print("Positions:\n", atoms_read.get_positions())
