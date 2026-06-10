from ase import Atoms
from ase.build import bulk

# Create Al BCC structure
al_bcc = bulk('Al', 'bcc', a=3.3, cubic=True)

# Print cell and chemical formula
print("Cell:\n", al_bcc.cell)
print("Chemical Formula:", al_bcc.get_chemical_formula())
