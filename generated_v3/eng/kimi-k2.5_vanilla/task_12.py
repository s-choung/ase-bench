from ase.build import bulk

atoms = bulk('Ti', 'hcp', a=2.95, c_over_a=1.59)

print("Cell vectors:")
print(atoms.get_cell())
print("\nAtomic positions:")
print(atoms.get_positions())
