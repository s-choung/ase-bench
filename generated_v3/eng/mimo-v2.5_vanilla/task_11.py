from ase.build import bulk

# Create BCC Al with a=3.3 Å, cubic cell
al = bulk('Al', 'bcc', a=3.3, cubic=True)

# Print cell and chemical formula
print("Cell vectors (in Angstroms):")
print(al.cell)
print(f"Chemical formula: {al.get_chemical_formula()}")
