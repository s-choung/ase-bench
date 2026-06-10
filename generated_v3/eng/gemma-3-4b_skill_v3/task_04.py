from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.build import molecule

# Create an H2O molecule
h2o = molecule('H2O')

# Set the EMT calculator
h2o.calc = EMT()

# Optimize the molecule
opt = BFGS(h2o)
opt.run(fmax=0.05, steps=1000)

# Print the initial and final energies
initial_energy = h2o.get_potential_energy()
final_energy = opt.get_final_potential_energy()

print(f"Initial energy: {initial_energy} eV")
print(f"Final energy: {final_energy} eV")
