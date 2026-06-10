from ase.build import bulk, surface
from ase.calculators.emt import EMT

# Cu bulk
cu = bulk('Cu', 'fcc', a=3.615)

# (2,1,1) surface, 3 layers, 10 Å vacuum
slab = surface(cu, (2, 1, 1), layers=3, vacuum=10.0)

# Attach a simple calculator
slab.set_calculator(EMT())

# Output
print('Number of atoms:', len(slab))
print('Cell:', slab.get_cell())
