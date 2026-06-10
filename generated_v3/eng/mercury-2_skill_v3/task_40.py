from ase import Atoms
from ase.build import bulk
from ase.io import write, read

# create NaCl rock‑salt crystal
na_cl = bulk('NaCl', 'rocksalt', a=5.64)

# save and reload as CIF
write('nacl.cif', na_cl, format='cif')
na_cl2 = read('nacl.cif', format='cif')

# space‑group info
sg = na_cl2.get_spacegroup()
print(f'Spacegroup: {sg.symbol} (#{sg.number})')
print(f'Number of atoms: {len(na_cl2)}')
