from ase.lattice.cubic import FaceCenteredCubic
from ase.build import surface

bulk = FaceCenteredCubic(size=(1,1,1), symbol='Cu', pbc=True)
slab = surface(bulk, (2,1,1), layers=3, vacuum=10.0)
print(f"Atoms: {len(slab)}, Cell:\n{slab.cell}")
