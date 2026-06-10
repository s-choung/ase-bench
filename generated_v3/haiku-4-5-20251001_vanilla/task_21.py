from ase.cluster.icosahedron import Icosahedron
from ase.calculators.emt import EMT

au_ico = Icosahedron('Au', noshells=3)
au_ico.set_calculator(EMT())

print(f"Number of atoms: {len(au_ico)}")
print(f"Center of mass: {au_ico.get_center_of_mass()}")
