from ase.build import bulk

# Create BCC Al with lattice constant 3.3 Å, enforce cubic cell
al = bulk('Al', crystalstructure='bcc', a=3.3, cubic=True)

print("Cell vectors (Å):")
print(al.get_cell())
print("\nChemical formula:", al.get_chemical_formula())
