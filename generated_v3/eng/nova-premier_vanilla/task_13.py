from ase import Atoms, Atom
from ase.build import bulk

a = 5.43
Si_bulk = bulk('Si', 'diamond', a=a)
supercell = Si_bulk.repeat((3, 3, 3))

print("Number of atoms:", len(supercell))
print("Cell volume:", supercell.get_volume())
