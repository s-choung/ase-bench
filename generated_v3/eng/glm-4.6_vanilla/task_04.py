from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create H2O molecule
h2o = Atoms('H2O', positions=[[0, 0, 0], [0.95, 0, 0], [0.237, 0.927, 0]])
h2o.calc = EMT()

# Initial energy
print(f"Initial energy: {h2o.get_potential_energy():.6f} eV")

# Optimize
opt = BFGS(h2o, logfile=None)
opt.run(fmax=0.01)

# Final energy
print(f"Final energy: {h2o.get_potential_energy():.6f} eV")
