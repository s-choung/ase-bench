from ase.build import mx2

atoms = mx2(formula='MoS2', kind='2H', a=3.18, thickness=3.19, vacuum=10.0)
print(atoms.cell)
