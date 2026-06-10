from ase.build import fcc111, add_vacuum
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms

slab = fcc111('Mo', size=(2, 2, 4), stacking=2)
slab.set_cell([[3.30, 0.0, 0.0], [0.0, 3.30, 0.0], [0.0, 0.0, 6.30]])
slab.wrap()

sulfur = fcc111('S', size=(2, 2, 4), stacking=2)
sulfur.set_cell([[3.30, 0.0, 0.0], [0.0, 3.30, 0.0], [0.0, 0.0, 6.30]])
sulfur.wrap()
sulfur.rotate(90, 'z')
sulfur.translate([0, 0, 3.3])

slab += sulfur

calc = EMT()
slab.calc = calc

slab = add_vacuum(slab, 10.0)

print(slab.cell)
