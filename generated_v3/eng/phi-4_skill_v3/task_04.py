from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create an H2O molecule
h2o = molecule('H2O')

# Set the calculator
h2o.calc = EMT()

# Print the potential energy before optimization
energy_before = h2o.get_potential_energy()
print(f"Potential energy before optimization: {energy_before} eV")

# Execute optimization using BFGS
opt = BFGS(h2o)
opt.run(steps=100, fmax=0.01)

# Print the potential energy after optimization
energy_after = h2o.get_potential_energy()
print(f"Potential energy after optimization: {energy_after} eV")
