from ase import bulk

# Create an Al BCC structure with a lattice constant of 3.3 Å
atoms = bulk('Al', 'bcc', a=3.3, cubic=True)

# Print the cell
print("Cell:")
print(atoms.get_cell())

# Print the chemical formula
print("Chemical formula:")
print(atoms.get_chemical_formula())
