from ase.build import mx2

atoms = mx2('MoS2')
atoms.center(vacuum=10, axis=2)
print(atoms.cell)
