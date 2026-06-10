from ase.build import bulk
from ase.calculators.emt import EMT
from ase.geometry import get_distances
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

p1 = atoms.positions[0:1]
p2 = atoms.positions[1:]
D, _ = get_distances(p1, p2, cell=atoms.cell, pbc=atoms.pbc)
distances = D[0]

print(distances.min())
print(distances.max())
