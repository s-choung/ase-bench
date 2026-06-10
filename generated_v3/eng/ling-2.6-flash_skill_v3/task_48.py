from ase import Atoms
from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True).repeat((2, 2, 2))
d, _ = get_distances(atoms.positions[0], atoms.positions, mic=True)
print('min:', d.min(), 'max:', d.max())
