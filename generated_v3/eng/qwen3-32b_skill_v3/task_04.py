from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

h2o = molecule('H2O')
h2o.calc = EMT()
print(f"Before optimization: {h2o.get_potential_energy():.4f} eV")
BFGS(h2o).run(fmax=0.05)
print(f"After optimization: {h2o.get_potential_energy():.4f} eV")
