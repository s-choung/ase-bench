from ase.build import bulk
atoms = bulk('Ti', 'hcp', a=2.95, c=2.95*1.59)
print(atoms.cell)
print(atoms.positions)
