from ase.build import mx2

mos2 = mx2('MoS2', kind='2H', a=3.18, thickness=3.17, vacuum=10.0)

print("Cell lengths (Å):", mos2.cell.lengths())
print("Cell angles (deg):", mos2.cell.angles())
