from ase.build import bulk
from ase.io import read, write
atoms = bulk('Au', 'fcc')
write('au.xyz', atoms, format='xyz')
atoms2 = read('au.xyz')
print(atoms2.get_chemical_symbols())
print(atoms2.get_positions())
