from ase.cluster import Octahedron
from ase.calculators.emt import EMT

cu = Octahedron('Cu', length=5, cutoff=0)
cu.calc = EMT()
print(len(cu), cu.positions.shape)
