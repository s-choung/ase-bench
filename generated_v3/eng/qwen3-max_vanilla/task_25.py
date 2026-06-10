from ase import Atoms
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

# Create FCC Cu bulk with initial lattice constant
a0 = 3.6
cu = Atoms('Cu', positions=[[0, 0, 0]], cell=[a0, a0, a0], pbc=True).repeat((2, 2, 2))
cu.calc = EMT()

# Print initial energy and cell size
print(f"Initial cell size: {cu.cell.lengths()[0]:.4f} Å")
print(f"Initial energy: {cu.get_potential_energy():.6f} eV")

# Optimize with FrechetCellFilter
opt = BFGS(FrechetCellFilter(cu))
opt.run(fmax=0.01)

# Print final energy and cell size
print(f"Final cell size: {cu.cell.lengths()[0]:.4f} Å")
print(f"Final energy: {cu.get_potential_energy():.6f} eV")
