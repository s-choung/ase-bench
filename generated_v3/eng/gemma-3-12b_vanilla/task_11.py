from ase.build import bulk
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms

atoms = bulk('Al', 'bcc', a=3.3)
atoms.calc = EMT()
atoms.set_constraint(FixAtoms(mask=[0, 1, 2, 3, 4, 5]))

print(atoms.cell)
print(atoms.get_chemical_formula())
