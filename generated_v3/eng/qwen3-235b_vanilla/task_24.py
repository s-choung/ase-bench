from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

# Create Au FCC bulk structure
au = bulk('Au')

# Set EMT calculator
au.calc = EMT()

# Optimize structure using LBFGS
opt = LBFGS(au, trajectory='opt.traj')
opt.run(fmax=0.01)

# Print number of steps and final energy
print(f"Number of steps: {len(opt)}}")
print(f"Final energy: {au.get_potential_energy():.4f}")
