from ase.build import bulk
from ase.io import write, read

au = bulk('Au', 'fcc', a=4.08)
write('au.xyz', au)
au_read = read('au.xyz')
print(au_read.get_chemical_symbols())
print(au_read.get_positions())
