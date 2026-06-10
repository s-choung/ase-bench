from ase import Atoms
from ase.build import bulk

a = 2.95
c = a * 1.59
Ti_bulk = bulk('Ti', 'hcp', a=a, c=c)

print("Cell vectors:")
print(Ti_bulk.get_cell())

print("\nAtomic positions:")
for pos in Ti_bulk.get_positions():
    print(pos)
