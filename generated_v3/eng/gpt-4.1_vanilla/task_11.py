from ase.build import bulk

a = 3.3
al_bcc = bulk('Al', 'bcc', a=a, cubic=True)
print('Cell:\n', al_bcc.cell)
print('Formula:', al_bcc.get_chemical_formula())
