from ase.cluster import Icosahedron
from ase.calculators.emt import EMT

atoms = Icosahedron('Au', noshells=3)
atoms.calc = EMT()
print(len(atoms), atoms.get_center_of_mass())
