from ase import Atoms
from ase.build import bulk
import numpy as np

a = 2.95
c_a = 1.59
c = a * c_a
unit_cell = bulk('Ti', crystalstructure='hcp', a=a, c=c, cubic=False)
print('Cell vectors:')
print(unit_cell.cell)
print('Atomic positions:')
print(unit_cell.get_positions())
