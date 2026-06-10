from ase.build import bulk
from ase.calculators.emt import EMT

atoms = bulk('Al', 'bcc', a=3.3, cubic=True)
atoms.calc = EMT()

print(atoms.cell)
print(atoms.get_chemical_formula())
