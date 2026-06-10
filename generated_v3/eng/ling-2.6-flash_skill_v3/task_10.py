from ase.cluster import Octahedron
from ase import Atoms

# Build a Cu octahedron with length=5 (scaled by default in Angstrom)
octa = Octahedron('Cu', length=5)

print('Number of atoms:', len(octa))
print('Positions shape:', octa.get_positions().shape)
