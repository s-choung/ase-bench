from ase.build import surface

atoms = surface('Fe', 'bcc', (1, 1, 0), layers=4, vacuum=10)
atoms *= (2, 2, 1)
print(len(atoms))
print(atoms.cell)
