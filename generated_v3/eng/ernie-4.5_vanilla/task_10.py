from ase.build import cut
from ase.cluster.octahedron import Octahedron
import ase.io as io

# Create a Cu Octahedron nanoparticle with length=5
atoms = Octahedron('Cu', length=5, cutoff=2)

# Print the number of atoms
print(f"Number of atoms: {len(atoms)}")

# Print the positions shape
print(f"Positions shape: {atoms.positions.shape}")

# Optional: Save the structure to a file for visualization
# io.write('cu_octahedron.xyz', atoms)
