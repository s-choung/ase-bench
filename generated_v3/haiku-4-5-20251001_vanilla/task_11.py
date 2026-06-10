from ase.build import bulk
from ase.calculators.emt import EMT

al_bcc = bulk('Al', 'bcc', a=3.3, cubic=True)
al_bcc.set_calculator(EMT())

print("Cell:")
print(al_bcc.cell)
print("\nChemical Formula:")
print(al_bcc.get_chemical_formula())
