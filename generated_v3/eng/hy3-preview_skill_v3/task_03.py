from ase.build import mx2, add_vacuum

mos2 = mx2('MoS2', kind='2H')
add_vacuum(mos2, 10)

print("Cell:")
print(mos2.get_cell())
print("\nCell lengths and angles (Å, deg):")
print(mos2.get_cell_lengths_and_angles())
