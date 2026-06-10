from ase import Atoms
from ase.build import nanoparticle

# Create Cu octahedron nanoparticle with length 5
atoms = nanoparticle('Cu', 'octahedron', length=5)

print(f"Number of atoms: {len(atoms)}")
print(f"Positions shape: {atoms.positions.shape}")
