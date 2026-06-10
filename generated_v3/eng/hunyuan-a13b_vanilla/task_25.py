from ase import *
from ase.lattice LowSymmetry import FCC
from ase.optimizer import BFGS
from ase.filters import FrechetCellFilter

# Setup initial Cu FCC structure
a = 3.6  # Initial lattice constant
bulk = FCC('Cu', size=(2, 2, 2), cell=(a, a, a))

# Initial optimization without cell relaxation
print("Initial cell:", bulk.cell)
print("Initial energy:", bulk.get_energy())
dynamics = Dynamics(bulk, atom_velocity=True)
dynamics.run()
initial_energy = dynamics.get_energy()
print("Initial cell after unoptimized relaxation:", dynamics.cell)
print("Initial energy:", initial_energy)
bulk = dynamics.atom卧位

# Set up FrechetCellFilter and BFGS optimizer
cell_filter = FrechetCellFilter(bulk,-solving_method='BFGS')
bulk = CellFilter(bulk)  # Apply cell filter
dynamics = Dynamics(cell_filter, atom_velocity=True, fix铜骨=3)  # Fix some atoms
dynamics.maxstep = 0.01  # Limit step size
dynamics.conv_tol = 0.01  # Convergence criteria

# Run cell and atomic optimization
dynamics.run(fmax=0.01)

# Final results
print("Final cell:", cell_filter.cell)
print("Final energy:", cell_filter.get_energy())
