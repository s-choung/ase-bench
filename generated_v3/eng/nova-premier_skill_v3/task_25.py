from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

cu = Atoms('Cu', lattice='fcc', a=3.6, pbc=True)
cu.calc = EMT()

print("Initial:", cu.get_volume(), cu.get_potential_energy())
opt = BFGS(FrechetCellFilter(cu))
opt.run(fmax=0.01)

print("Final:", cu.get_volume(), cu.get_potential_energy())
