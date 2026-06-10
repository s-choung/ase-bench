from ase.build import bulk

# Create Al BCC structure
atoms = bulk('Al', 'bcc', a=3.3, cubic=True)

# Print the cell and chemical formula
cell = atoms.get_cell()
chemical_formula = atoms.get_chemical_formula()

print("Cell dimensions:", cell)
print("Chemical formula:", chemical_formula)
