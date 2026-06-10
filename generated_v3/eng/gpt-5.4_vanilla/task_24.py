from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc', a=4.08)
atoms.calc = EMT()

opt = LBFGS(atoms, logfile=None)
opt.run(fmax=0.01)

print(opt.nsteps)
print(atoms.get_potential_energy())
