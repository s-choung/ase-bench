from ase.build import fcc111, molecule
from ase.optimize import BFGS
from ase.constraints import FixAtoms

slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)
n2 = molecule('N2')
from ase.build import add_adsorbate
add_adsorbate(slab, n2, height=2.0, position='bridge')
slab.set_constraint(FixAtoms(mask=[a.tag >= 3 for a in slab]))
from ase.calculators.emt import EMT
slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

print(len(slab))
print(set([atom.symbol for atom in slab]))
