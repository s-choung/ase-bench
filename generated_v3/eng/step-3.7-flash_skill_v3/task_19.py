from ase import Atoms
from ase.geometry import get_distances

atoms = Atoms(['C', 'O', 'O'], [[0, 0, 0], [1.16, 0, 0], [-1.16, 0, 0]], cell=[10, 10, 10], pbc=False)
dists = get_distances(atoms.positions, atoms.positions)[0]
for i in range(len(atoms)):
    for j in range(i + 1, len(atoms)):
        print(f"{atoms.symbols[i]}-{atoms.symbols[j]}: {dists[i, j]:.2f} Å")
