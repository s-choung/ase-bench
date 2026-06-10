from ase import Atoms
from ase.build import bulk
from ase.optimize import BFGS
from ase.constraints import ExpCellFilter
from ase.calculators.emt import EMT

# Initialize Cu FCC bulk
cu = bulk('Cu', 'fcc', a=3.6)
cu.calc = EMT()

# Print initial values
print("Initial cell size:", cu.get_cell().tolist())
print("Initial energy:", cu.get_potential_energy())

# Set up optimization
optimize = BFGS(ExpCellFilter(cu), trajectory=None, logfile=None)

# Run optimization
optimize.run(fmax=0.01)

# Print final values
print("Final cell size:", cu.get_cell().tolist())
print("Final energy:", cu.get_potential_energy())
