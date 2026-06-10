from ase.build import fcc100
from ase.calculators.emt import EMT

atoms = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)
atoms.calc = EMT()
print(len(atoms), atoms.cell)
