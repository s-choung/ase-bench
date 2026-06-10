from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FrechetCellFilter
from ase.optimize import BFGS
from ase.optimize.fire import FIRE

# Create Cu FCC bulk structure
a0 = 3.6  # Initial lattice constant
cu = Atoms('Cu',
           positions=[(0, 0, 0), (0.5, 0.5, 0), (0.5, 0, 0.5), (0, 0.5, 0.5)],
           cell=[[a0, 0, 0], [0, a0, 0], [0, 0, a0]],
           pbc=True)
cu.set_calculator(EMT())

# Print initial state
print(f"Initial cell size: {cu.cell.cellparities()}")
print(f"Initial energy: {cu.get_potential_energy():.6f}")

# Set up optimization with FrechetCellFilter and BFGS
constraint = FrechetCellFilter(cu)
optimizer = BFGS(constraint)
optimizer.run(fmax=0.01)

# Print final state
print(f"Final cell size: {cu.cell.cellparities()}")
print(f"Final energy: {cu.get_potential_energy():.6f}")
