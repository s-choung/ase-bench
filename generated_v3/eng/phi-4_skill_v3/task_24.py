from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
from ase.constraints import FixInternals
from ase.io import Trajectory

# Create a bulk Au structure with an FCC lattice
atoms = bulk('Au', 'fcc', a=4.08, cubic=True)

# Set EMT calculator
atoms.set_calculator(EMT())

# Apply symmetry constraints (optional, can be skipped if not necessary)
constraints = FixInternals(atoms)

# Initialize the LBFGS optimizer with a trajectory file to monitor the process
opt = LBFGS(atoms, trajectory='opt.traj', logfile='opt.log')

# Add constraints to the optimizer
opt.run(fmax=0.01, steps=-1)

# Print the number of optimization steps and the final energy
print("Optimization completed in", opt.iterations, "steps.")
print("Final energy:", atoms.get_potential_energy(), "eV")
