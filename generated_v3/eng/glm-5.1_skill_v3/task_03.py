from ase.build import mx2

mos2 = mx2('MoS2', vacuum=10)
print(mos2.cell)
