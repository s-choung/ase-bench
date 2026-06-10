from ase import Atoms
from ase.spacegroup import crystal

# Create NaCl crystal structure
atoms = crystal('NaCl', [(0, 0, 0)], spacegroup=225, cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

# Save NaCl crystal structure in CIF format
atoms.write('nacl.cif')

# Read back NaCl crystal structure from CIF file
new_atoms = read('nacl.cif')

print('Spacegroup:', new_atoms.get_spacegroup())
print('Number of atoms:', len(new_atoms))
