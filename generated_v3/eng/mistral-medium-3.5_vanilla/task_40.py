from ase.build import bulk
from ase.io import write, read

# Create and save NaCl rock-salt structure
structure = bulk('NaCl', 'rocksalt', a=5.64)
write('nacl.cif', structure, format='cif')

# Read back and print info
atoms = read('nacl.cif', format='cif')
print(f"Spacegroup: {atoms.info['spacegroup']}")
print(f"Number of atoms: {len(atoms)}")
