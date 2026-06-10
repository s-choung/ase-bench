from ase.build import bulk
from ase.calculators.emt import EMT
from ase.constraints import UnitCellFilter
from ase.optimize import LBFGS

atoms = bulk('Au', cubic=True)
atoms.calc = EMT()
ucf = UnitCellFilter(atoms)
opt = LBFGS(ucf)
opt.run(fmax=0.01)
print(opt.nsteps)
print(atoms.get_potential_energy())
