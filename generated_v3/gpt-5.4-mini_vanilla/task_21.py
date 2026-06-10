from ase.cluster.icosahedron import Icosahedron
from ase.calculators.emt import EMT

atoms = Icosahedron('Au', noshells=3)
atoms.calc = EMT()

print("Number of atoms:", len(atoms))
print("Center of mass:", atoms.get_center_of_mass())
