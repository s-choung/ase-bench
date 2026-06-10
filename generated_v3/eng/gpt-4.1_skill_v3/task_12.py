from ase.build import bulk
from ase import units

a = 2.95
c = 1.59 * a
atoms = bulk('Ti', 'hcp', a=a, c=c)
print('Cell vectors (Å):')
print(atoms.get_cell())
print('\nAtomic positions (Å):')
print(atoms.get_positions())
