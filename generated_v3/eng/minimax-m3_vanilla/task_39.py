from ase.build import bulk
from ase.io import read, write

# Create Au FCC bulk
atoms = bulk('Au', 'fcc', a=4.08)

# Save to XYZ file
write('au_bulk.xyz', atoms)

# Read back
atoms_read = read('au_bulk.xyz')

# Print atom types and positions
print("Atom types:", atoms_read.get_chemical_symbols())
print("Positions:")
for atom in atoms_read:
    print(f"  {atom.symbol}: {atom.position}")
