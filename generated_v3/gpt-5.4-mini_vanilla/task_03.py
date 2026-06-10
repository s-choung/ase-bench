from ase.build import mx2

atoms = mx2('MoS2', kind='2H', a=3.18, thickness=3.13, size=(1, 1, 1), vacuum=10.0)

print(atoms.cell)
