from ase.build import bulk

a = 2.95
c = a * 1.59
atoms = bulk('Ti', 'hcp', a=a, c=c)

print(atoms.cell)
print(atoms.positions)
