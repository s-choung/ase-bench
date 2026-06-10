from ase.cluster import Icosahedron
from ase.calculators.emt import EMT

au_ico = Icosahedron('Au', noshells=3)
au_ico.calc = EMT()
print(len(au_ico))
print(au_ico.get_center_of_mass())
