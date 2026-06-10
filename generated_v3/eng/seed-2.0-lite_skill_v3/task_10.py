from ase.cluster import Octahedron

# Create Cu octahedron nanoparticle with length=5
cu_np = Octahedron('Cu', length=5)

# Output required values
print(f"Number of atoms: {len(cu_np)}")
print(f"Positions array shape: {cu_np.get_positions().shape}")
