from ase.build import bulk
from ase.optimize import BFGS
from ase.constraints import FrechetCellFilter
from ase.calculators.emt import EMT

cu = bulk('Cu', 'fcc', a=3.6, cubic=True)
cu.calc = EMT()

print(f"Initial cell: {cu.cell.cellpar()}, Energy: {cu.get_potential_energy():.3f} eV")

opt = BFGS(FrechetCellFilter(cu), trajectory=None)
opt.run(fmax=0.01)

print(f"Optimized cell: {cu.cell.cellpar()}, Energy: {cu.get_potential_energy():.3f} eV")
