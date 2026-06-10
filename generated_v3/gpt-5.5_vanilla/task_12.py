from ase.build import bulk

a = 2.95
c = a * 1.59

atoms = bulk("Ti", "hcp", a=a, c=c)

print("Cell vectors:")
print(atoms.cell)

print("\nAtomic positions:")
for i, atom in enumerate(atoms):
    print(i, atom.symbol, atom.position)
