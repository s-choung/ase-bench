from ase.build import bulk

a = 2.95
c = a * 1.59          # c/a = 1.59
atoms = bulk('Ti', 'hcp', a=a, c=c)

print("Cell vectors:\n", atoms.cell)
print("Atomic positions:\n", atoms.positions)
