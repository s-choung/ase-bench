from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

h2o = Atoms('H2O', positions=[(0.0, 0.0, 0.0), (0.74, 0.0, 0.0), (0.37, 0.65, 0.0)])
h2o.calc = EMT()

energy_initial = h2o.get_potential_energy()
print(f'Initial energy: {energy_initial:.4f} eV')

optimizer = BFGS(h2o)
optimizer.run(fmax=0.01)

energy_final = h2o.get_potential_energy()
print(f'Final energy: {energy_final:.4f} eV')
