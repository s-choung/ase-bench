from ase.cluster import Octahedron

# Create a Cu octahedron nanoparticle with length 5
atoms = Octahedron('Cu', length=5)

# Print the number of atoms and the positions shape
num_atoms = len(atoms)
positions_shape = atoms.positions.shape

print(f'Number of atoms: {num_atoms}')
print(f'Positions shape: {positions_shape}')
