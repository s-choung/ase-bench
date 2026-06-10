from ase.build import fcc111, molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)
co = molecule('CO')
co.translate([slab.cell[0, 0]/4, slab.cell[1, 1]/4, slab.positions[:, 2].max() + 1.8])
slab += co

slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

print(len(slab))
