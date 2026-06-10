from ase.build import bulk

a = 2.95
covera = 1.59

atoms = bulk('Ti', 'hcp', a=a, covera=covera)

print("Cell vectors:")
print(atoms.cell)

print("\nAtomic positions:")
for i, pos in enumerate(atoms.positions):
    print(f"{i:2d} {atoms[i].symbol} {pos}")
