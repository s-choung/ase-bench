from ase.build import mx2
mos2 = mx2('MoS2')
mos2.center(vacuum=10, axis=2)
print(mos2.cell)
