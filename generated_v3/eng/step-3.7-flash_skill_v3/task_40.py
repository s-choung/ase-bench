from ase.spacegroup import crystal
from ase.io import read, write

# Generate NaCl rock-salt structure and save to CIF
nacl = crystal('NaCl', basis=[(0, 0, 0), (0.5, 0.5, 0.5)], spacegroup=225, cellpar=[5.64, 5.64, 5.64, 90, 90, 90])
write('nacl.cif', nacl, format='cif')

# Read CIF back and print info
atoms = read('nacl.cif', format='cif')
sg = atoms.info['spacegroup']
print(f"Space group: {sg['symbol']} (No. {sg['number']})")
print(f"Number of atoms: {len(atoms)}")
