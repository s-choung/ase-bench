from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

# Create Au FCC bulk structure
atoms = bulk('Au', 'fcc', a=4.078)

# Set the EMT calculator
atoms.calc = EMT()

# Initialize and run the optimizer
opt = LBFGS(atoms, logfile=None)
opt.run(fmax=0.01)

# Print number of steps and final energy
print("Number of optimization steps:", len(opt.get_trajectory()))
print("Final energy:", atoms.get_potential_energy())
