from ase.build import bulk

al_bcc = bulk('Al', crystalstructure='bcc', a=3.3, cubic=True)

print("Cell:\n", al_bcc.cell[:])
print("Chemical Formula:", al_bcc.get_chemical_formula())
