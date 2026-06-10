from ase.build import bulk

al = bulk('Al', 'bcc', a=3.3, cubic=True)
print(al.cell)
print(al.get_chemical_formula())
