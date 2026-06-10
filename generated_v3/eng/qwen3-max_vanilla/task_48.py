from ase.build import bulk
from ase import Atoms

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
distances = atoms.get_distances(0, range(len(atoms)), mic=True)
print(distances.min(), distances.max())
