from ase.cluster import Octahedron
from ase.calculators.emt import EMT

atoms = Octahedron('Cu', length=5)
print(len(atoms), atoms.positions.shape)
