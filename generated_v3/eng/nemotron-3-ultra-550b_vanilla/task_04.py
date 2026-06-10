from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create H2O molecule
h2o = Atoms('H2O', positions=[(0, 0, 0), (0.75, 0.59, 0), (-0.75, 0.59, 0)])

# Attach EMT calculator
h2o.calc = EMT()

# Print initial energy
print(f"Initial energy: {h2o.get_potential_energy():.6f} eV")

# Optimize with BFGS
opt = BFGS(h2o, trajectory=None, logfile=None)
opt.run(fmax=0.05)

# Print final energy
print(f"Final energy: {h2o.get_potential_energy():.6f} eV")
