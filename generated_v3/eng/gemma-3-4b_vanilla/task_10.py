from ase import atoms
from ase.build import fcc111
from ase.calculators import EMT

a = 5.0
c = a * 1.18 # Lattice constant for Cu(111)
atoms = fcc111('Cu', a=a, c=c, symmetry='placental')
atoms.set_calculator(EMT())
print(len(atoms))
print(atoms.get_positions().shape)
