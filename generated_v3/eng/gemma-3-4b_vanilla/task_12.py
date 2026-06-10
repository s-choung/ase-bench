from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import fcc111

a = 2.95
c_a = 1.59
c = a * c_a

calc = EMT()
atoms = fcc111('Ti', size=(4, 4, 4), a=a, c=c, size_set='large')
atoms.set_calculator(calc)
calc.xc = 'modified_gga'
calc.kpts = (4, 4, 1)
atoms.get_cell()
print("Cell vectors:", atoms.get_cell())
print("Atomic positions:", atoms.get_positions())
