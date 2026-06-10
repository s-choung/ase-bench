from ase.build import nanotube
from ase.calculators.emt import EMT

nt = nanotube(6, 6, length=4)
nt.calc = EMT()
print(nt.get_number_of_atoms())
print(nt.get_cell())
