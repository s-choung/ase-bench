from ase.build import bulk
from ase.cluster.octahedron import Octahedron

atoms = Octahedron('Cu', length=5)

print(f"Number of atoms: {len(atoms)}")
print(f"Positions shape: {atoms.positions.shape}")
