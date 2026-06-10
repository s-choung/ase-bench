from ase import Atoms
from ase.build import bulk

atoms = bulk('Al', 'bcc', a=3.3, cubic=True)

print("Cell:", atoms.get_cell())
print("Chemical Formula:", atoms.get_chemical_formula())
