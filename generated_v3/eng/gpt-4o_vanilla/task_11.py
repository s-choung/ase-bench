from ase.build import bulk

aluminum_bcc = bulk('Al', 'bcc', a=3.3, cubic=True)
print("Cell:")
print(aluminum_bcc.cell)
print("Chemical Formula:", aluminum_bcc.get_chemical_formula())
