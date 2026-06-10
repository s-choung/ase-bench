from ase import Atoms
from ase.lattice.atomic import HCP

a = 2.95
c = a * 1.59

structure = HCP('Ti', a=a, c=c, cubic=False)
print("Cell vectors:")
print(structure.cell)
print("Atomic positions:")
print(structure.positions)
