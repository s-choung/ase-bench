from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# Initial structure
a = 3.6
cu = Atoms('Cu', positions=[[0, 0, 0]], cell=[[a/2, a/2, 0], [a/2, 0, a/2], [0, a/2, a/2]], pbc=True)
cu *= (2, 2, 2)

# Calculator and initial output
cu.calc = EMT()
print(f'Initial cell size: {cu.cell.lengths()}')
print(f'Initial energy: {cu.get_potential_energy()}')

# Optimization
fcf = FrechetCellFilter(cu)
opt = BFGS(fcf)
opt.run(fmax=0.01)

# Final output
print(f'Optimized cell size: {cu.cell.lengths()}')
print(f'Optimized energy: {cu.get_potential_energy()}')
