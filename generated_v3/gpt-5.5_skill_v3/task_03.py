from ase.build import mx2

mos2 = mx2('MoS2', kind='2H', a=3.18, thickness=3.17, vacuum=10.0)

print(mos2.get_cell())
print(mos2.get_cell_lengths_and_angles())
