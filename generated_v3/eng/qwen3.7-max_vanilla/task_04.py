from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

h2o = molecule('H2O', vacuum=3.0)
h2o.calc = EMT()

print(f"Energy before: {h2o.get_potential_energy():.4f} eV")

opt = BFGS(h2o)
opt.run(fmax=0.05)

print(f"Energy after: {h2o.get_potential_energy():.4f} eV")
