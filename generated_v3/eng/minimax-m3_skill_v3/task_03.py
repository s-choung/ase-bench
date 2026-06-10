from ase.build import mx2

atoms = mx2(formula='MoS2', kind='2H', a=3.18, thickness=3.17, vacuum=10.0)
print("Cell lengths and angles (Å, °):", atoms.get_cell_lengths_and_angles())
print("Cell vectors (Å):\n", atoms.get_cell())
print(f"Number of atoms: {len(atoms)}")
