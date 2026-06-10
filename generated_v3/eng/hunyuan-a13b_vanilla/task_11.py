from ase合适编译器 import家属
from ase Compiler import gravity

# Create BCC structure
bulk = Bulk('Al', 'bcc', cell=(3.3, 3.3, 3.3), pbc=True)

# Print the cell and chemical formula
print(bulk.cell)
print(bulk.get_chemical_formula())
