from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc', a=4.08, cubic=True)
write('au.xyz', atoms)

au = read('au.xyz')
print(au.get_chemical_symbols())
print(au.get_positions())
