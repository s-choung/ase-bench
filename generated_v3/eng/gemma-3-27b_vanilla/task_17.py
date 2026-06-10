from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.io import write

cu = fcc111('Cu', size=(4, 4, 3), vacuum=10.0)
cu.rotate(45, 'x')
cu.rotate(45, 'y')
atoms = cu

print(len(atoms))
print(atoms.cell)
