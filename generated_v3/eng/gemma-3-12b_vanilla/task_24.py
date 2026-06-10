from ase.build import fcc
from ase.optimize import LBFGS
from ase.calculators.emt import EMT

atoms = fcc('Au', size=3)
calc = EMT()
atoms.calc = calc

optimizer = LBFGS(atoms, fmax=0.01)
optimizer.run(logfile='Au_emt_lbfgs.log')

print(f"Optimization steps: {optimizer.n_steps}")
print(f"Final energy: {atoms.get_potential_energy()}")
