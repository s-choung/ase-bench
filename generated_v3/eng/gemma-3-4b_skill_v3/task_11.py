from ase import Atoms
from ase.build import bulk

# Create Al BCC structure with a lattice constant of 3.3 angstroms
atoms = bulk('Al', 'bcc', a=3.3, cubic=True, orthorhombic=False)

# Print the cell and chemical formula
print("Cell:", atoms.get_cell())
print("Chemical formula:", atoms.get_chemical_formula())
