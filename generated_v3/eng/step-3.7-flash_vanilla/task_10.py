from ase.cluster import Octahedron
from ase.calculators.emt import EMT

cu_octa = Octahedron('Cu', length=5, latticeconstant=3.615)
cu_octa.calc = EMT()
print(len(cu_octa))
print(cu_octa.positions.shape)
