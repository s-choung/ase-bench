from ase.build import bulk

# Create aluminum BCC with a=3.3 Å
Al_BCC = bulk('Al', 'bcc', a=3.3, cubic=True)

# Print the cell representation and chemical formula
print(Al_BCC)
print(Al_BCC.get_chemical_formula())
