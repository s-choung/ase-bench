from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

h2o = Atoms('H2O', positions=[(0.75, 0.5, 0), (-0.75, 0.5, 0), (0, 0, 0)])
h2o.set_calculator(EMT())

e_init = h2o.get_potential_energy()
dyn = BFGS(h2o)
dyn.run(fmax=0.01)

print("Initial Energy:", e_init)
print("Final Energy:", h2o.get_potential_energy())
