from ase.build import bulk
from ase import Atoms

atoms = bulk('Al', 'bcc', a=3.3, cubic=True)
print("Cell:", atoms.get_cell())
print("Chemical formula:", atoms.get_chemical_formula())
