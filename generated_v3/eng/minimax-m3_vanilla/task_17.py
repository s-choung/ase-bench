from ase.build import bulk, surface
from ase.constraints import FixAtoms

cu = bulk('Cu', 'fcc', a=3.6)
slab = surface(cu, (2, 1, 1), layers=3, vacuum=10.0)

print(f"Number of atoms: {len(slab)}")
print(f"Cell:\n{slab.cell}")
