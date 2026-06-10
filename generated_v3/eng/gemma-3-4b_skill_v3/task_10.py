from ase import Atoms
from ase.cluster import Octahedron
from ase.visualize import view

# Create a Cu Octahedron nanoparticle
atoms = Octahedron('Cu', length=5)

# Print the number of atoms
print(f"Number of atoms: {len(atoms)}")

# Print the shape of the positions array
print(f"Shape of positions array: {atoms.positions.shape}")

# Visualize the structure (optional)
# view(atoms)
