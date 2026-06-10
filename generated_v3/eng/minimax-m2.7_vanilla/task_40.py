from ase.build import nacl
from ase.io import write, read

# create NaCl (rock‑salt) structure
atoms = nacl()

# write to CIF
write('NaCl.cif', atoms)

# read back
atoms = read('NaCl.cif')

# spacegroup info
sg = atoms.info.get('spacegroup')
print('Spacegroup:', sg.symbol if sg else 'unknown')
print('Spacegroup number:', sg.no if sg else 'unknown')

# number of atoms
print('Number of atoms:', len(atoms))
