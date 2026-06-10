from ase import Atoms
from ase.build import bulk
from ase.io import read, write

# Create an Au FCC bulk
atoms = bulk('Au', 'fcc', a=3.6)

# Write the atoms to an XYZ file
write('Au_bulk.xyz', atoms)

# Read the XYZ file back
atoms_read = read('Au_bulk.xyz')

# Print the atom types and positions
print("Atom Types:")
for atom in atoms_read:
    print(atom.type)

print("\nAtom Positions:")
for atom in atoms_read:
    print(atom.positions)
