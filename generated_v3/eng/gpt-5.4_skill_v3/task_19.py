from ase import Atoms
from ase.geometry import get_distances
import numpy as np

atoms = Atoms(
    symbols='CO2',
    positions=[(0.0, 0.0, 0.0), (-1.16, 0.0, 0.0), (1.16, 0.0, 0.0)],
    cell=(10.0, 10.0, 10.0),
    pbc=False,
)

pos = atoms.get_positions()
d01 = get_distances(pos[0], pos[1])[1][0, 0]
d02 = get_distances(pos[0], pos[2])[1][0, 0]
d12 = get_distances(pos[1], pos[2])[1][0, 0]

print(f"C-O(1): {d01:.2f} Å")
print(f"C-O(2): {d02:.2f} Å")
print(f"O-O: {d12:.2f} Å")
