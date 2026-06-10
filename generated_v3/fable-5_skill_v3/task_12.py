from ase.build import bulk

a = 2.95
c = a * 1.59
atoms = bulk('Ti', 'hcp', a=a, c=c)

print("Cell vectors:")
print(atoms.get_cell())
print("\nPositions:")
for atom in atoms:
    print(atom.symbol, atom.position)
