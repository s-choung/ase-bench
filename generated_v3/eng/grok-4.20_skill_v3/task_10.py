from ase.cluster import Octahedron
from ase.calculators.emt import EMT

atoms = Octahedron('Cu', length=5)
atoms.calc = EMT()

print(len(atoms))
print(atoms.get_positions().shape)
