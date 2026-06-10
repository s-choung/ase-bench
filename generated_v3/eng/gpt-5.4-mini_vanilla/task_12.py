from ase.build import bulk

ti = bulk('Ti', 'hcp', a=2.95, c=2.95 * 1.59)

print("Cell vectors:")
print(ti.cell)

print("\nAtomic positions:")
for i, pos in enumerate(ti.positions):
    print(f"Atom {i}: {pos}")
