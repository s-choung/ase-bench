from ase.build import bulk

atoms = bulk('Al', 'bcc', a=3.3, cubic=True)
print(atoms.get_cell())
print(atoms.get_chemical_formula())
