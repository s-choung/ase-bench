from ase import Atoms
from ase.build import bulk

a = 3.3
atoms = bulk('Al', crystalstructure='bcc', a=a, cubic=True)
print('Cell:', atoms.cell)
print('Chemical formula:', atoms.get_chemical_formula())
