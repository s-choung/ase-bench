from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
from ase.optimize.precon import PreconLBFGS

# Create Au FCC bulk structure
atoms = bulk('Au', 'fcc', a=4.08)
atoms.calc = EMT()

# Optimize structure using LBFGS optimizer with fmax=0.01
opt = LBFGS(atoms, trajectory='Au_opt.traj')
opt.run(fmax=0.01)

# Print number of optimization steps and final energy
print("Optimization steps:", opt.optimizer.get_number_of_steps())
print("Final energy:", atoms.get_potential_energy())
