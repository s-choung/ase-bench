from ase import Atoms
from ase.build import bulk

cu_bulk = bulk('Cu', 'fcc', a=3.6)
cu_supercell = cu_bulk * (2, 2, 2)

print(cu_supercell.cell)
print(len(cu_supercell))
