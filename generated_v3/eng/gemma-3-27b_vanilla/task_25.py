from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.constraints import FixedPlane

cu = fcc111('Cu', size=(3, 3, 3), vacuum=1.0)

print("Initial cell size:", cu.cell.shape)
print("Initial energy:", cu.get_potential_energy())

calc = EMT()
cu.calc = calc

dyn = BFGS(cu, trajectory='cu_optimization.traj',
           filters=[FrechetCellFilter(0.01)],
           optimizer='BFGS')

dyn.run(fmax=0.01)

print("Final cell size:", cu.cell.shape)
print("Final energy:", cu.get_potential_energy())
