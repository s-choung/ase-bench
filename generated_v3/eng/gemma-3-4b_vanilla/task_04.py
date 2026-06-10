from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import write

# Build the H2O molecule
molecules = molecule('H2O', size=20)

# Set the EMT calculator
calc = EMT()
molecules.set_calculator(calc)

# Optimize the molecule
dyn = BFGS(molecules, trajectory='h2o_optimization.traj')
dyn.run(fmax=0.01)

# Print the energy before and after optimization
print("Energy before optimization:", molecules.get_potential_energy())
print("Energy after optimization:", molecules.get_potential_energy())

# Write the optimized structure to a file
write('h2o_optimized.xyz', molecules)
