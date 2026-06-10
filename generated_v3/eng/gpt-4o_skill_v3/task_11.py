from ase.build import bulk

atoms = bulk('Al', 'bcc', a=3.3, cubic=True)
cell = atoms.get_cell()
formula = atoms.get_chemical_formula()

print("Cell:")
print(cell)

print("\nChemical Formula:")
print(formula)
