from ase.build import bulk, surface, add_vacuum
from ase.calculators.emt import EMT

# bulk Cu (fcc)
cu_bulk = bulk('Cu', 'fcc', a=3.6)

# cut (2,1,1) surface with 3 layers
slab = surface(cu_bulk, (2, 1, 1), layers=3, vacuum=0.0, periodic=True)

# add 10 Å vacuum in z‑direction
add_vacuum(slab, 10.0)

# optional calculator (built‑in EMT)
slab.calc = EMT()

# output
print('Number of atoms:', len(slab))
print('Cell vectors (Å):')
print(slab.get_cell())
