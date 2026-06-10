from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

atoms = bulk("Cu", "fcc", a=3.8, cubic=True)
atoms.calc = EMT()

print("Before cell:")
print(atoms.cell)
print("Before energy:", atoms.get_potential_energy())

ucf = FrechetCellFilter(atoms)
opt = BFGS(ucf, logfile=None)
opt.run(fmax=0.01)

print("After cell:")
print(atoms.cell)
print("After energy:", atoms.get_potential_energy())
