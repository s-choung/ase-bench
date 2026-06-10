from ase.build import bulk

atoms = bulk('Al', 'bcc', a=3.3, cubic=True)

print("Cell:")
print(atoms.get_cell())

print("\nChemical Formula:")
print(atoms.get_chemical_formula())
