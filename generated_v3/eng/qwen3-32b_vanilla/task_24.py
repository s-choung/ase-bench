from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc', cubic=True)
atoms.calc = EMT()
opt = LBFGS(atoms, fmax=0.01)
opt.run()
print(f"Optimization steps: {opt.nsteps}")
print(f"Final energy: {atoms.get_potential_energy()} eV")
