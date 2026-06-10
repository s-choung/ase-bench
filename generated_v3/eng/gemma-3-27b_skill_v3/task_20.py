from ase import Atoms
from ase.build import nanotube

atoms = nanotube(6, 6, length=4)

print(len(atoms))
print(atoms.get_cell())
