from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.lattice.cubic import FaceCenteredCubic

cu = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                      symbol='Cu', size=(1, 1, 1))
cu.calc = EMT()

print(f"Initial cell size: {cu.get_cell()[0, 0]:.2f} Å, Energy: {cu.get_potential_energy():.2f} eV")

dyn = BFGS(FrechetCellFilter(cu), trajectory='cu_opt.traj')
dyn.run(fmax=0.01)

print(f"Optimized cell size: {cu.get_cell()[0, 0]:.2f} Å, Energy: {cu.get_potential_energy():.2f} eV")
