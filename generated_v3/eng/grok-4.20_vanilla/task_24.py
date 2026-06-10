from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc', a=4.078)
atoms.calc = EMT()

opt = LBFGS(atoms, logfile=None)
opt.run(fmax=0.01)

print(len(opt.converged_steps), atoms.get_potential_energy())
