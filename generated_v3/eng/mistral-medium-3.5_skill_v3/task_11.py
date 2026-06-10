from ase import bulk
from ase.calculators.emt import EMT

al = bulk('Al', 'bcc', a=3.3, cubic=True)
al.calc = EMT()
print(al.get_chemical_formula(), al.get_cell())
