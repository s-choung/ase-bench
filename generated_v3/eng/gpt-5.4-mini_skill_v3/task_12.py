from ase.build import bulk

atoms = bulk('Ti', 'hcp', a=2.95, c=2.95 * 1.59)

print("Cell vectors:")
print(atoms.cell)

print("\nAtomic positions:")
for i, pos in enumerate(atoms.get_positions()):
    print(i, pos)
