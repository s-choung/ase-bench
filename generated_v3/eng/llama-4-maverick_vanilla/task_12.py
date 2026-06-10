from ase import Atoms
from ase.build import bulk

ti_hcp = bulk('Ti', 'hcp', a=2.95, c=2.95*1.59)
print(ti_hcp.cell)
print(ti_hcp.positions)
