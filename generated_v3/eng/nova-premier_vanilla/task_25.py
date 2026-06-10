from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FrechetCellFilter

a0 = 3.6  # Initial lattice constant guess
cu = Atoms('Cu', cell=[[a0, 0, 0], [0, a0, 0], [0, 0, a0]], pbc=True)
cu *= (2, 2, 2)
cu.calc = EMT()

e0 = cu.get_potential_energy()
print(f"Initial cell size: {cu.get_volume()}")
print(f"Initial energy: {e0}")

opt = BFGS(FrechetCellFilter(cu), trajectory=None)
opt.run(fmax=0.01)

e_final = cu.get_potential_energy()
print(f"Final cell size: {cu.get_volume()}")
print(f"Final energy: {e_final}")
