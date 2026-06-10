from ase.build import bulk

atoms = bulk('Ti', 'hcp', a=2.95, covera=1.59)

print("Cell vectors:")
print(atoms.cell[:])
print("\nAtomic positions:")
print(atoms.positions)
