from ase.build import bulk

# Create BCC aluminum bulk structure
al_bcc = bulk('Al', 'bcc', a=3.3, cubic=True)

# Output requested properties
print("Unit cell matrix (Å):\n", al_bcc.get_cell())
print("\nChemical formula:", al_bcc.get_chemical_formula())
