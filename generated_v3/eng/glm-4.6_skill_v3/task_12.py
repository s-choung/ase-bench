from ase.build import bulk

atoms = bulk('Ti', 'hcp', a=2.95, covera=1.59)

print(atoms.cell)
print(atoms.positions)
