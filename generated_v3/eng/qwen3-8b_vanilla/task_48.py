from ase.build import bulk
from ase import Atoms

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True).repeat([2,2,2])
dist = atoms.get_distances([0], list(range(1, len(atoms))), mic=True)
print(f"Min: {min(dist)}, Max: {max(dist)}")
