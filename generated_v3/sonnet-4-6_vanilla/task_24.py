from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc', a=4.08)
atoms.calc = EMT()

optimizer = LBFGS(atoms, logfile=None)
optimizer.run(fmax=0.01)

print(f"Optimization steps: {optimizer.get_number_of_steps()}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
