from ase.build import bulk

a = 2.95
c = 1.59 * a
atoms = bulk('Ti', 'hcp', a=a, c=c)

print("Cell vectors:")
print(atoms.get_cell()[:])
print("\nAtomic positions:")
for atom in atoms:
    print(f"{atom.symbol} {atom.position}")
