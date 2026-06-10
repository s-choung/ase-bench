from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic

# Create Cu octahedron nanoparticle with length=5 (in lattice constants)
length = 5
cu_atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                             size=(length, length, length),
                             symbol='Cu',
                             pbc=False)

# Truncate to octahedron shape
positions = cu_atoms.get_positions()
center = positions.mean(axis=0)
distance_from_center = ((positions - center)**2).sum(axis=1)**0.5
max_distance = distance_from_center.max()
cutoff = max_distance / (length / 2.5)  # Approximate octahedron cutoff

# Keep atoms within octahedron boundary (Manhattan distance style)
mask = (abs(positions[:, 0] - center[0]) + 
        abs(positions[:, 1] - center[1]) + 
        abs(positions[:, 2] - center[2]) <= 2.5 * length)

cu_octahedron = cu_atoms[mask]

# Print results
print("Number of atoms:", len(cu_octahedron))
print("Positions shape:", cu_octahedron.get_positions().shape)
