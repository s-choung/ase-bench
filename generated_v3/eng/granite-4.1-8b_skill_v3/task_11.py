from ase import Atoms
from ase.build import bulk

# Create Al BCC structure
atoms = bulk('Al', 'bcc', a=3.3, cubic=True)

# Print cell and chemical formula
print(atoms.cell)
print(atoms.get_chemical_formula())
