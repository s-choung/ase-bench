from ase import Atoms
from ase.build import nanotube
from ase.io import write

# Create a Cu Octahedron nanoparticle with length=5
cu_octahedron = Atoms('Cu8', positions=[
    (0, 0, 0),
    (2.5, 0, 0),
    (0, 2.5, 0),
    (0, 0, 2.5),
    (2.5, 2.5, 0),
    (2.5, 0, 2.5),
    (0, 2.5, 2.5),
    (2.5, 2.5, 2.5)
], cell=[5, 5, 5], pbc=False)

# Correct approach: Use FCC lattice for octahedron
from ase.build import make_crystal
cu_octahedron = make_crystal('Cu', [(0, 0, 0), (0.5, 0.5, 0), (0.5, 0, 0.5), (0, 0.5, 0.5)], size=(2, 2, 2))
cu_octahedron.positions += [2.5, 2.5, 2.5]  # Center at (2.5, 2.5, 2.5)

# Print number of atoms and positions shape
print("Number of atoms:", len(cu_octahedron))
print("Positions shape:", cu_octahedron.positions.shape)
