from ase.build import mx2, add_vacuum

mos2 = mx2('MoS2', kind='2H', vacuum=0)
add_vacuum(mos2, 10.0)
print(mos2.get_cell_lengths_and_angles())
