from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc', a=4.08)
atoms.calc = EMT()

opt = LBFGS(atoms, logfile=None)
opt.run(fmax=0.01)

print("Optimization steps:", opt.nsteps)
print("Final energy (eV):", atoms.get_potential_energy())
