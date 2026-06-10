from ase.build import bulk

# Create BCC Al with a = 3.3 Å, enforce cubic cell
atoms = bulk('Al', 'bcc', a=3.3, cubic=True)

# Output cell vectors and chemical formula
print("Cell (Å):")
print(atoms.get_cell())
print("Formula:", atoms.get_chemical_formula())
