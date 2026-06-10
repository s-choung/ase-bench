from ase.cluster import Octahedron
from ase import Atoms

atoms = Octahedron('Cu', length=5)

print(len(atoms))
print(atoms.get_positions().shape)
