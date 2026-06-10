import numpy as np
from ase.cluster.cubic import FaceCenteredCubic
from ase.calculators.emt import EMT

def create_octahedron(size):
    # Generate FCC atoms (Cu is FCC)
    # A size of 5 implies a specific number of shells/layers
    # For a perfect octahedron, we filter atoms by Manhattan distance from center
    atoms = FaceCenteredCubic(size=size, symbol='Cu')
    
    # Find center of mass/geometry
    center = atoms.get_center_of_mass()
    
    # Get positions and lattice vector (a = 3.61 for Cu)
    pos = atoms.get_positions()
    a = 3.61
    
    # In FCC, distance to center in units of lattice constant helps define octahedron
    # A simple way to form an octahedron is to constrain atoms where |x|+|y|+|z| <= limit
    # We transform coordinates to lattice units first
    lattice_coords = pos / (a / np.sqrt(2))
    
    # Calculate Manhattan distance from center in lattice units
    # For size 5, we need to define the "radius" of the octahedron
    # We'll filter atoms to keep those within a certain Manhattan distance
    dist = np.sum(np.abs(lattice_coords - center / (a / np.sqrt(2))), axis=1)
    
    # Threshold for size 5 octahedron (approximate based on FCC lattice)
    mask = dist <= (size - 1)
    atoms.positions = pos[mask]
    
    return atoms

# Create Cu octahedron with size 5
cluster = create_octahedron(5)
cluster.set(calculator=EMT())

print(f"Number of atoms: {len(cluster)}")
print(f"Positions shape: {cluster.positions.shape}")
