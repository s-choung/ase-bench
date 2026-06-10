from ase import Atoms
from ase.build import bulk

a = 2.95
c_over_a = 1.59
atoms = bulk('Ti', 'hcp', a=a, c=a*c_over_a)

print("Cell vectors:")
for v in atoms.cell:
    print(v)

print("\nAtomic positions:")
for pos in atoms.positions:
    print(pos)
