from ase.build import fcc
from ase.calculators.emt import EMT
from ase.units import Angstrom

si = fcc('Si', size=(3, 3, 3), latticeconstant=5.43 * Angstrom)
calc = EMT()
si.calc = calc

print(len(si))
print(si.get_volume())
