from ase import Atoms
from ase.spacegroup import crystal
from ase.io import read, write

# Build NaCl structure
atoms = crystal(('Na', 'Cl'), spacegroup=225, cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

# Save to CIF format
write('nacl.cif', atoms)

# Read structure
atoms = read('nacl.cif')

# Analysis
print("Spacegroup:", atoms.info['spacegroup'])
print("Atom count:", len(atoms))
