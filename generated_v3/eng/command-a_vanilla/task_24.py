from ase import Atoms
from ase.optimize import LBFGS
from ase.calculators.emt import EMT
from ase.lattice.cubic import FaceCenteredCubic

# Create Au FCC bulk structure
au = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                       size=(2, 2, 2), symbol='Au')

# Attach EMT calculator
au.calc = EMT()

# Initialize LBFGS optimizer
opt = LBFGS(au, trajectory=None, logfile=None)

# Run optimization
num_steps = opt.irun(fmax=0.01)

# Print results
print(f'Number of steps: {num_steps}')
print(f'Final energy: {au.get_potential_energy():.6f} eV')
