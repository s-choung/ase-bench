from ase.build import bulk
from ase.io import read, write

# Create Au FCC bulk
atoms = bulk('Au', 'fcc', a=4.08)

# Save to XYZ file
write('au_fcc.xyz', atoms)

# Read back from XYZ file
atoms_read = read('au_fcc.xyz')

# Print atom types and positions
print("Atom types:", atoms_read.get_chemical_symbols())
print("Positions:")
print(atoms_read.get_positions())
