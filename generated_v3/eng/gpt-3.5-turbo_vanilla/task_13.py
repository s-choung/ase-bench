from ase import Atoms
from ase.build import bulk

a = 5.43
atoms = bulk("Si", crystalstructure="diamond", a=a)

supercell = atoms*(3, 3, 3)

print("Number of atoms:", len(supercell))
print("Cell volume:", supercell.get_volume())
