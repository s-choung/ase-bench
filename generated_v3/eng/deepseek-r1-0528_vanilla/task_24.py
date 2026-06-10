from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = bulk('Au', cubic=True)
atoms.calc = EMT()
dyn = LBFGS(atoms, logfile=None)
steps = dyn.run(fmax=0.01)
energy = atoms.get_potential_energy()

print(f'Number of optimization steps: {steps}')
print(f'Final energy: {energy} eV')
