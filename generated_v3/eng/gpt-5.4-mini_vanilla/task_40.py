from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import get_spacegroup

# Build NaCl crystal
atoms = bulk('NaCl', 'rocksalt', a=5.64)

# Save to CIF
write('nacl.cif', atoms)

# Read back from CIF
atoms2 = read('nacl.cif')

# Spacegroup info and atom count
sg = get_spacegroup(atoms2)
print(sg)
print('Number of atoms:', len(atoms2))
