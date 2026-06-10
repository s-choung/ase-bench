from ase.build import bulk

al_bcc = bulk('Al', cubic=True, a=3.3, crystalstructure='bcc')
print(al_bcc.cell)
print(al_bcc.get_chemical_formula())
