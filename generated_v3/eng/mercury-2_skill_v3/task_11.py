from ase import Atoms
from ase.build import bulk

# Create BCC Al with a = 3.3 Å, enforce cubic cell
al = bulk('Al', 'bcc', a=3.3, cubic=True)

# Output cell parameters and chemical formula
print("Cell matrix (Å):")
print(al.get_cell())
print("Formula:", al.get_chemical_formula())
