from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
from ase.filters import UnitCellFilter

atoms = bulk("Au", "fcc", a=4.2, cubic=True)
atoms.calc = EMT()

ucf = UnitCellFilter(atoms)
opt = LBFGS(ucf, logfile=None)
opt.run(fmax=0.01)

print("Optimization steps:", opt.nsteps)
print("Final energy:", atoms.get_potential_energy())
