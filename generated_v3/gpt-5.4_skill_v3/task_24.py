from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Au', 'fcc', a=4.08, cubic=True)
atoms.calc = EMT()

opt = LBFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print(opt.nsteps)
print(atoms.get_potential_energy())
