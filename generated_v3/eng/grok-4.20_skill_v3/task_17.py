from ase.build import bulk, surface
from ase.io import write

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True)
slab = surface(atoms, (2, 1, 1), layers=3, vacuum=10.0)
print(len(slab))
print(slab.get_cell())
