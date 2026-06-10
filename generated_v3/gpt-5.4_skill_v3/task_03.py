from ase.build import mx2, add_vacuum

atoms = mx2('MoS2', kind='2H', a=3.18, thickness=3.17)
add_vacuum(atoms, 10.0)

print(atoms.get_cell())
print(atoms.get_cell_lengths_and_angles())
