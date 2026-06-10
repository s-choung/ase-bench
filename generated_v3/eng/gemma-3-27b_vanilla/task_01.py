from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import write

cu = fcc111('Cu', size=(2, 2, 2), vacuum=10.0)
print(cu.cell)
print(len(cu))

calc = EMT()
cu.calc = calc
dyn = BFGS(cu, trajectory='cu_fcc.traj')
dyn.run(fmax=0.02)

write('cu_fcc.xyz', cu)
