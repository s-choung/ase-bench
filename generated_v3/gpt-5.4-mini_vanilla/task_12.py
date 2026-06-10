from ase.build import bulk

a = 2.95
c = a * 1.59

atoms = bulk('Ti', 'hcp', a=a, c=c)

print("Cell vectors (Angstrom):")
print(atoms.cell)

print("\nAtomic positions (Angstrom):")
for i, pos in enumerate(atoms.positions):
    print(f"{i}: {pos}")
