from ase.build import molecule
from ase.optimize import BFGS
from ase.calculators.emt import EMT

h2o = molecule('H2O')
calc = EMT()
h2o.calc = calc

print("Initial energy:", h2o.get_potential_energy())

optimizer = BFGS(h2o, trajectory='h2o_emt_opt.traj')
optimizer.run(fmax=0.05)

print("Final energy:", h2o.get_potential_energy())
