from ase.build import bulk

# Create an Al BCC structure with a lattice constant of 3.3 angstroms
al_bcc = bulk('Al', cubic=True, a=3.3)

# Print the cell and chemical formula
print(al_bcc)
print(al_bcc.formula)
