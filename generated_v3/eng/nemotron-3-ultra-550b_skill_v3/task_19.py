from ase import Atoms
import numpy as np

positions = [(0.0, 0.0, 0.0), (-1.16, 0.0, 0.0), (1.16, 0.0, 0.0)]
atoms = Atoms('COO', positions=positions, cell=(10.0, 10.0, 10.0), pbc=False)

d01 = atoms.get_distances(0, [1])[0]
d02 = atoms.get_distances(0, [2])[0]
d12 = atoms.get_distances(1, [2])[0]

print(f"C-O (1): {d01:.3f} Å")
print(f"C-O (2): {d02:.3f} Å")
print(f"O-O:     {d12:.3f} Å")
