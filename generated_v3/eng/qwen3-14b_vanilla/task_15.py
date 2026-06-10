from ase.build import bulk, surface
from ase import Atoms

atoms = bulk('Cu', 'fcc')
slab = surface(atoms, (1, 0, 0), layers=3, vacuum=12, repeat=(3, 3))
print(len(slab))
print(slab.get_cell())
