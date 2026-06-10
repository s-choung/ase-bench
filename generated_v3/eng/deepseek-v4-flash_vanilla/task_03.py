from ase.build import mx2

atoms = mx2('MoS2')
atoms.center(vacuum=10, axis=2)

print("Cell size (angstroms):", atoms.get_cell_lengths_and_angles()[:3])
