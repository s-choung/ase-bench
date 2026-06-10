from ase.build import mx2

slab = mx2(formula='MoS2', vacuum=10.0)
print(slab.cell)
