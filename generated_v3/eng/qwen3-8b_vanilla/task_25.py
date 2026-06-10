import ase
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.set_calculator(EMT())

print("Initial cell:", atoms.get_cell())
print("Initial energy:", atoms.get_energy())

fc = FrechetCellFilter(atoms)
opt = BFGS(fc, fmax=0.01)
opt.run()

print("Optimized cell:", atoms.get_cell())
print("Optimized energy:", atoms.get_energy())
