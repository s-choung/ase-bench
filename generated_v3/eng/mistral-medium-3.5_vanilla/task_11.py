from ase.lattice.cubic import BodyCenteredCubic
from ase import Atoms

al = BodyCenteredCubic(size=(1,1,1), symbol="Al", pbc=True, latticeconstant=3.3)
print(al.get_chemical_formula(), al.get_cell())
