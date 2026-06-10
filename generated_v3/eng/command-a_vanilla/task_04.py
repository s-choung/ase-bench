from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import write

# Define the H2O molecule
h2o = Atoms('HOH', positions=[(0, 0, 0), (0, 0.957, -0.111), (0, -0.257, 0.111)], calculator=EMT())

# Print initial energy
print(f"Initial energy: {h2o.get_potential_energy():.6f} eV")

# Optimize geometry using BFGS
dyn = BFGS(h2o, trajectory='h2o_opt.traj')
dyn.run(fmax=0.01)

# Print final energy
print(f"Final energy: {h2o.get_potential_energy():.6f} eV")

# Write optimized structure
write('h2o_opt.xyz', h2o)
