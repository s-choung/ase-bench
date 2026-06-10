from ase.cluster import Octahedron

# Create Cu Octahedron nanoparticle
cu_octahedron = Octahedron('Cu', length=5)

# Get number of atoms and positions shape
num_atoms = len(cu_octahedron)
positions_shape = cu_octahedron.get_positions().shape

# Print results
print(f"Number of atoms: {num_atoms}")
print(f"Positions shape: {positions_shape}")
