from ase.cluster import Icosahedron
from ase.calculators.emt import EMT

# Build Au icosahedron with 3 shells
atoms = Icosahedron('Au', noshells=3, latticeconstant=4.08)
atoms.calc = EMT()  # optional calculator

print(len(atoms))                 # number of atoms
print(atoms.get_center_of_mass()) # center of mass (Å)
