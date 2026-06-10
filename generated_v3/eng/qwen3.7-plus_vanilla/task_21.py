from ase.cluster import Icosahedron
from ase.calculators.emt import EMT

atoms = Icosahedron('Au', 3)
atoms.calc = EMT()

print(len(atoms))
print(atoms.get_center_of_mass())
