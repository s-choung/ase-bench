from ase.build import bulk
from ase import Atoms

cu_bulk = bulk('Cu', 'fcc', a=3.6, cubic=True)
cu_supercell = cu_bulk * (2, 2, 2)

print("Cell Information:", cu_supercell.get_cell())
print("Number of Atoms:", len(cu_supercell))
