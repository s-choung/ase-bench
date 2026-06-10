from ase.build import fcc100

slab = fcc100('Cu', size=(3,3,3), vacuum=12)
print(f"Number of atoms: {len(slab)}")
print(f"Cell dimensions (Å):\n{slab.cell}")
print(f"Cell lengths (Å): {slab.cell.lengths()}")
print(f"Cell angles (°): {slab.cell.angles()}")
