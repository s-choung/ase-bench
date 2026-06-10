from ase.build import nanotube
from ase import Atoms
from ase.calculators.emt import EMT

atoms = nanotube(n=6, m=6, length=4)
atoms.set_calculator(EMT())
print(len(atoms))
print(atoms.get_cell())
