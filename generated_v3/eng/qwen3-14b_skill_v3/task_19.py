from ase import Atoms
from ase.geometry import get_distances

atoms = Atoms(symbols=['C', 'O', 'O'],
              positions=[[0, 0, 0], [1.16, 0, 0], [-1.16, 0, 0]],
              cell=[[10, 0, 0], [0, 10, 0], [0, 0, 10]],
              pbc=False)
distances = get_distances(atoms, mic=False)
print(f"Interatomic distances: {distances} Å")
