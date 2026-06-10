from ase.build import bulk

# Create Aluminum BCC structure
atoms = bulk('Al', 'bcc', a=3.3, cubic=True)

# Print cell and chemical formula
print(f"Cell:\n{atoms.get_cell()}")
print(f"Formula: {atoms.get_chemical_formula()}")
