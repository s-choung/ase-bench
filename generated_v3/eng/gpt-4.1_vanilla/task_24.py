from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc', a=4.08)
atoms.calc = EMT()
opt = LBFGS(atoms, logfile=None)
nsteps = opt.run(fmax=0.01)
print(f"Optimization steps: {nsteps}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
