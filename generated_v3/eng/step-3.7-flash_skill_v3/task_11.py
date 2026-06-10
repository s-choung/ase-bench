from ase.build import bulk

al_bcc = bulk('Al', 'bcc', a=3.3, cubic=True)
print("Unit cell (Å):\n", al_bcc.cell)
print("Chemical formula:", al_bcc.get_chemical_formula())
