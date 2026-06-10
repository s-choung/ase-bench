from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.61, cubic=True) * (2, 2, 2)
_, d = get_distances(atoms.positions[0].reshape(1, 3), atoms.positions,
                     cell=atoms.cell, pbc=atoms.pbc, mic=True)
d = d[0]
print(d[1:].min(), d.max())
