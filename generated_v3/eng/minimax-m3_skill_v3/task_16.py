from ase.build import bcc110

slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)
print(f"Number of atoms: {len(slab)}")
print(f"Cell (Å):\n{slab.cell[:]}")
print(f"Cell lengths (a, b, c): {slab.cell.lengths()}")
