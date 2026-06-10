from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc')
atoms.calc = EMT()
opt = LBFGS(atoms, logfile=None)
nsteps = opt.run(fmax=0.01)
energy = atoms.get_potential_energy()
print('Optimization steps:', nsteps)
print('Final energy (eV):', energy)
