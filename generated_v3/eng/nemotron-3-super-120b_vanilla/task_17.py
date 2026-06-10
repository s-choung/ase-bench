from ase import Atoms
from ase.build import bulk, surface
from ase.calculators.emt import EMT

# bulk Cu
cu = bulk('Cu', 'fcc', a=3.615)
# cut (2,1,1) surface, 3 layers, 10 Å vacuum
slab = surface(cu, (2,1,1), layers=3, vacuum=10.0)
# attach a simple calculator (optional)
slab.set_calculator(EMT())

print(f'Number of atoms: {len(slab)}')
print('Cell:')
print(slab.cell)
