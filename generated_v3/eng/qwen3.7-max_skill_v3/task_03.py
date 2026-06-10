from ase.build import mx2, add_vacuum

atoms = mx2('MoS2')
add_vacuum(atoms, 10.0)
print(atoms.get_cell_lengths_and_angles())
