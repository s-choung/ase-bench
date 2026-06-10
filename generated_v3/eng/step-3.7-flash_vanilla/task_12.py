from ase.build import bulk

atoms = bulk('Ti', 'hcp', a=2.95, c_over_a=1.59)
print("Cell vectors (Å):\n", atoms.cell)
print("Atomic positions (Å):\n", atoms.get_positions())
