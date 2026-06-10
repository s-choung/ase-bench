from ase.build import bulk

atoms = bulk('Al', 'bcc', a=3.3, cubic=True)
print("Cell:")
print(atoms.cell)
print("Chemical Formula:", atoms.get_chemical_formula())
