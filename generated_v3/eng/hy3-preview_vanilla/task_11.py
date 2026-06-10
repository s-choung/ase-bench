from ase.build import bulk

al = bulk('Al', 'bcc', a=3.3, cubic=True)
print("Cell:", al.cell)
print("Formula:", al.get_chemical_formula())
