from ase.build import bulk
from ase import Atoms

# Create BCC Al structure
al_bcc = bulk('Al', 'bcc', a=3.3, cubic=True)

# Print the cell parameters and chemical formula
print("Cell parameters:")
print(al_bcc.cell)
print("Chemical formula:")
print(al_bcc.get_chemical_formula())
