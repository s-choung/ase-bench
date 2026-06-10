from ase.build import fcc111
from ase import Atoms

slab = fcc111("Cu", size=(2, 2, 1), vacuum=None, cubic=True)
atoms = slab.repeat((1, 1, 2))

d = atoms.get_distances(0, indices=range(len(atoms)), mic=True)
print("min:", d[1:].min(), "max:", d[1:].max())
