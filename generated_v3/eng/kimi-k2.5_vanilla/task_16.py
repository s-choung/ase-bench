from ase.build import bcc110

slab = bcc110('Fe', a=2.87, size=(2, 2, 4), vacuum=10.0)

print(f"Number of atoms: {len(slab)}")
print(f"Cell size: {slab.cell.lengths()}")
