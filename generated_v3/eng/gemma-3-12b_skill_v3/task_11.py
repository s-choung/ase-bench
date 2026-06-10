from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT

atoms = bulk('Al', 'bcc', a=3.3)
atoms.calc = EMT()

print(atoms.get_cell())
print(atoms.get_chemical_formula())
