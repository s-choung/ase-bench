"""T9 Wiki: Relax cell + positions simultaneously for bulk Cu"""
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

cu = bulk('Cu', 'fcc', a=3.5)
cu.calc = EMT()

fcf = FrechetCellFilter(cu)
opt = BFGS(fcf)
opt.run(fmax=0.01)
print(f"Optimized cell: {cu.get_cell()}")
print(f"Energy: {cu.get_potential_energy():.4f} eV")
print(f"Volume: {cu.get_volume():.4f} Å³")
