from ase import Atoms
import numpy as np

a = 3.18
d = 1.55
s3 = np.sqrt(3)
a1 = [a, 0, 0]
a2 = [-a/2, a*s3/2, 0]
positions = [
    [0, 0, 0],
    [0, a/s3, d],
    [a/2, a*s3/6, -d]
]
atoms = Atoms('MoS2', positions=positions, cell=[a1, a2, [0, 0, 1]], pbc=(True, True, False))
atoms.center(vacuum=10.0, axis=2)
print(atoms.cell.lengths())
