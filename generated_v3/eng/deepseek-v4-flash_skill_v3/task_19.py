from ase import Atoms
from ase.geometry import get_distances

atoms = Atoms('CO2', positions=[[0.0, 0.0, 0.0],
                                 [1.16, 0.0, 0.0],
                                 [-1.16, 0.0, 0.0]],
              cell=[10, 10, 10], pbc=False)

pos = atoms.get_positions()
dist_matrix, _ = get_distances(pos, pos)
for i in range(len(atoms)):
    for j in range(i + 1, len(atoms)):
        print(f'{atoms[i].symbol}-{atoms[j].symbol}: {dist_matrix[i][j]:.4f}')
