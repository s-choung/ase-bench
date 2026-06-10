from ase import Atoms
from ase.build import bulk

a = 2.95
c_over_a = 1.59
ti_hcp = bulk('Ti', 'hcp', a=a, c=a * c_over_a)

print("Cell vectors:")
for vector in ti_hcp.cell:
    print(vector)

print("\nAtomic positions:")
for position in ti_hcp.positions:
    print(position)
