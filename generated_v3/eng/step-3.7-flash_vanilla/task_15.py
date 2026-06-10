from ase.build import fcc100

slab = fcc100('Cu', size=(3, 3, 3), vacuum=12)
print(f"Number of atoms: {len(slab)}")
print(f"Cell vectors (Å):\n{slab.cell}")
