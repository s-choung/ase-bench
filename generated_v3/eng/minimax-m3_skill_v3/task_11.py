from ase.build import bulk
from ase.io import write

atoms = bulk('Al', 'bcc', a=3.3, cubic=True)
print(atoms.cell)
print(atoms.get_chemical_formula())
