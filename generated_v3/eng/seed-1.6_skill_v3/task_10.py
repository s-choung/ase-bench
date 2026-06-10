from ase.cluster import Octahedron

cu_octa = Octahedron('Cu', length=5)
print(len(cu_octa))
print(cu_octa.positions.shape)
