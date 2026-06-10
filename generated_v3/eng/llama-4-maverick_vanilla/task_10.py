from ase.cluster import Octahedron
from ase.calculators.emt import EMT

cu_octahedron = Octahedron('Cu', length=5, cutoff=2)
cu_octahedron.calc = EMT()

print(len(cu_octahedron))
print(cu_octahedron.positions.shape)
