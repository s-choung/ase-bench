from ase.build import bcc110

slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)
print(f"Number of atoms: {len(slab)}")
cell = slab.get_cell()
print(f"Cell:\n{cell}")
