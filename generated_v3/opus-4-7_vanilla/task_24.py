from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
from ase.constraints import ExpCellFilter

atoms = bulk('Au', 'fcc', a=4.08)
atoms.calc = EMT()

ecf = ExpCellFilter(atoms)
opt = LBFGS(ecf)
opt.run(fmax=0.01)

print("Steps:", opt.nsteps)
print("Final energy:", atoms.get_potential_energy())
