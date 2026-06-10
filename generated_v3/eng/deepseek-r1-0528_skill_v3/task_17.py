from ase.build import bulk, surface
from ase.build import add_vacuum

atoms = bulk('Cu', 'fcc', a=3.60)
slab = surface(atoms, (2, 1, 1), layers=3)
add_vacuum(slab, 10.0)

print("Number of atoms:", len(slab))
print("Cell (Å):")
print(slab.get_cell())
