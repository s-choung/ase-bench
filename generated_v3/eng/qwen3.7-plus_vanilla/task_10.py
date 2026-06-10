from ase.cluster.cubic import Octahedron
from ase.calculators.emt import EMT

atoms = Octahedron(symbols='Cu', n=5)
atoms.calc = EMT()

print(len(atoms))
print(atoms.positions.shape)
