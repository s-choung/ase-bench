from ase.build import bulk
from ase.geometry import get_distances
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
p0 = atoms.positions[0]
others = atoms.positions[1:]
d = get_distances(p0, others, cell=atoms.cell, pbc=atoms.pbc, mic=True)[0].flatten()
print(f"Min: {np.min(d):.4f} Å")
print(f"Max: {np.max(d):.4f} Å")
