from ase.build import bulk
from ase.calculators.emt import EMT
from ase.constraints import UnitCellFilter
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc', cubic=True)
atoms.calc = EMT()

ucf = UnitCellFilter(atoms)
opt = LBFGS(ucf, logfile=None)
opt.run(fmax=0.01)

print(opt.get_number_of_steps())
print(atoms.get_potential_energy())
