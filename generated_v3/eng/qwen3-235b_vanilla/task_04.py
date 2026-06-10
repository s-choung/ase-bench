from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create H2O molecule
h2o = Atoms('H2O',
            positions=[[0.76, -0.48, 0.0],
                       [-0.76, -0.48, 0.0],
                       [0.0, 0.13, 0.0]])

# Set EMT calculator
h2o.calc = EMT()

# Print energy before optimization
print("Energy before optimization:", h2o.get_potential_energy())

# Optimize with BFGS
opt = BFGS(h2o, trajectory='h2o.traj')
opt.run(fmax=0.05)

# Print energy after optimization
print("Energy after optimization:", h2o.get_potential_energy())
