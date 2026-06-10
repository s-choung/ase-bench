from ase.build import bulk, surface, add_vacuum
slab = surface(bulk('Cu', 'fcc', a=3.6), (2, 1, 1), layers=3)
add_vacuum(slab, 10)
print(f"Number of atoms: {len(slab)}")
print("Cell matrix (Å):\n", slab.cell)
