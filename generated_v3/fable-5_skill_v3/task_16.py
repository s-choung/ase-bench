from ase.build import bcc110

slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

print("원자 수:", len(slab))
print("Cell:")
print(slab.cell)
print("Cell 길이/각도:", slab.cell.cellpar())
