from ase.build import bulk
from ase.lattice.hexagonal import Hexagonal

a = 2.95
c = a * 1.59

atoms = bulk('Ti', 'hcp', a=a, c=c)

print("Cell vectors:")
print(atoms.cell)
print("\nAtomic positions:")
print(atoms.get_positions())
print("\nLattice parameters:")
print(f"a = {a}")
print(f"c = {c}")
print(f"c/a = {c/a}")
