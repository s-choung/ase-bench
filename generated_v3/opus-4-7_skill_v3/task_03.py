from ase.build import mx2

atoms = mx2('MoS2', kind='2H', a=3.18, thickness=3.17, vacuum=10.0)
print(atoms.get_cell())
print("Cell lengths and angles:", atoms.get_cell_lengths_and_angles())
