from ase.build import mx2

atoms = mx2('MoS2', kind='2H', vacuum=10.0)
print(atoms.get_cell())
