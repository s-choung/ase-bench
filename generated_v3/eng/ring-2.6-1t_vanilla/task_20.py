from ase.build import nanotube
from ase.calculators.emt import EMT

atoms = nanotube((6, 6), length=4)
atoms.calc = EMT()

print("Number of atoms:", len(atoms))
print("Cell:\n", atoms.cell)
