from ase.build import bulk

al_bcc = bulk('Al', 'bcc', a=3.3, cubic=True)

print("Cell:")
print(al_bcc.cell)

print("\nChemical Formula:")
print(al_bcc.get_chemical_formula())
