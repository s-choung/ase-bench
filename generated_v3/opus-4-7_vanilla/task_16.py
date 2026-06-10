from ase.build import bcc110

slab = bcc110('Fe', size=(2, 2, 4), a=2.87, vacuum=10.0)
print("원자 수:", len(slab))
print("Cell 크기:", slab.get_cell())
