from ase.build import bulk
from ase.io import write, read

# Build NaCl crystal, save CIF, read back
atoms = bulk('NaCl', 'rocksalt', a=5.64)
write('NaCl.cif', atoms)
atoms2 = read('NaCl.cif')

# Print spacegroup and number of atoms
print('Spacegroup:', atoms2.info.get('spacegroup'))
print('Number of atoms:', len(atoms2))
