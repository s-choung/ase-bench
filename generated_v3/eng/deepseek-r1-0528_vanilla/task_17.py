from ase.build import bulk, surface
from ase.visualize import view

atoms = bulk('Cu', 'fcc', a=3.6)
slab = surface(atoms, (2,1,1), 3)
slab.center(vacuum=10.0, axis=2)
print(f"Atoms: {len(slab)}")
print("Cell:")
for vector in slab.cell:
    print(vector)
