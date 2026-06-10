from ase.build import surface
from ase import Atoms

atoms = surface(crystal='Cu', indices=(2, 1, 1), layers=3, vacuum=10.0)

print(len(atoms))
print(atoms.get_cell())
