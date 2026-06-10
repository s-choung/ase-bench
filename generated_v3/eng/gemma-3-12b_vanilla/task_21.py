from ase.build import *
from ase.calculators.emt import EMT
from ase.io import write

icosahedron = icosahedron(size=3, symbol='Au', noshells=3)

calc = EMT()
icosahedron.calc = calc

print(len(icosahedron))
print(icosahedron.get_center_of_mass())

write('Au_icosahedron.xyz', icosahedron)
