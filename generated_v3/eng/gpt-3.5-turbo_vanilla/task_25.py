from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import UnitCellFilter

# Create Cu FCC bulk
a = 3.6  # initial guess for lattice constant
cu = Atoms('Cu',
           scaled_positions=[(0, 0, 0),
                             (0.5, 0.5, 0),
                             (0.5, 0, 0.5),
                             (0, 0.5, 0.5)],
           cell=(a, a, a),
           pbc=True)

cu.set_calculator(EMT())

# Initial cell size and energy
print('Initial cell size:', cu.get_cell_lengths_and_angles())
print('Initial energy:', cu.get_potential_energy())

# Optimization
ufilter = UnitCellFilter(cu)
opt = BFGS(ufilter, logfile=None)
opt.run(fmax=0.01)

# Final cell size and energy
print('Final cell size:', cu.get_cell_lengths_and_angles())
print('Final energy:', cu.get_potential_energy())
