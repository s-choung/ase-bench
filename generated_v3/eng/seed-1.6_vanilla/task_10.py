from ase.cluster import Nanoparticle
from ase.calculators.emt import EMT

radius = 5 / (2 ** 0.5)  # Edge length 5 Å (octahedron edge = radius×√2)
cu_octa = Nanoparticle('Cu', shape='octahedron', radius=radius)
cu_octa.calc = EMT()

print(len(cu_octa))
print(cu_octa.positions.shape)
