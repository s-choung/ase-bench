from ase.build import bcc110

slab = bcc110('Fe', size=(2,2,4), vacuum=10.0)
print(f"Number of atoms: {len(slab)}")
print(f"Cell:\n{slab.get_cell()}")
print(f"Cell lengths and angles: {slab.cell.cellpar()}")
