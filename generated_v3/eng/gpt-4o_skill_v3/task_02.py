from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111('Pt', size=(1, 1, 4), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')
slab.set_constraint(FixAtoms(mask=[a.tag >= 3 for a in slab]))
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

print(len(slab))
