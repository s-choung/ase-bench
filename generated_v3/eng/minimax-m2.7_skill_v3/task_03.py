from ase.build import mx2

atoms = mx2('MoS2', a=3.18, thickness=3.17, vacuum=10)
print(f"Cell size: {atoms.get_cell_lengths_and_angles()}")
