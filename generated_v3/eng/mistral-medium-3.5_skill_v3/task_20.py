from ase.build import nanotube
from ase.calculators.emt import EMT

atoms = nanotube(6, 6, length=4, symbol='C')
atoms.calc = EMT()
print(len(atoms), atoms.cell)
