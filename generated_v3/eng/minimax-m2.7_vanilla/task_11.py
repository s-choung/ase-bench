from ase.build import bulk

# Create Al BCC bulk structure with lattice constant a = 3.3 Å
al = bulk('Al', 'bcc', a=3.3, cubic=True)

print("Cell:")
print(al.get_cell())
print("\nChemical formula:", al.get_chemical_formula())
