from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

slab = fcc111('Pt', (4, 4, 4), vacuum=10.0)
constraint = FixAtoms(mask=[False] * len(slab))
slab.set_constraint(constraint)

co = add_adsorbate(slab, 'CO', atop=True, position='ontop')

calc = EMT()
co.calc = calc

opt = BFGS(co, trajectory='co_on_pt.traj')
opt.run(fmax=0.02)

print(len(co))
