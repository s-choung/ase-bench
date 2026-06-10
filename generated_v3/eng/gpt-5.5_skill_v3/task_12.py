from ase.build import bulk

a = 2.95
c = a * 1.59

atoms = bulk("Ti", "hcp", a=a, c=c)

print("Cell vectors (Å):")
print(atoms.cell.array)

print("\nAtomic positions (Å):")
for i, atom in enumerate(atoms):
    print(i, atom.symbol, atom.position)
