from ase.build import mx2

mos2 = mx2(formula='MoS2', kind='2H')
mos2.center(vacuum=10.0, axis=2)
print(mos2.cell.lengths())
