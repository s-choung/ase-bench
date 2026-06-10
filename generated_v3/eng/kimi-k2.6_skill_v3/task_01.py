from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.61, cubic=True)
atoms *= (2, 2, 2)

print(atoms.get_cell())
print(atoms.get_cell_lengths_and_angles())
print(len(atoms))
