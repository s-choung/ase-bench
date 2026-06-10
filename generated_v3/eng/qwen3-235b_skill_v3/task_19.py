from ase import Atoms
from ase.geometry import get_distances

atoms = Atoms('CO2', positions=[(0, 0, 0), (-1.16, 0, 0), (1.16, 0, 0)], 
              cell=(10, 10, 10), pbc=False)

dists, _ = get_distances(atoms.get_positions())
print(dists)
