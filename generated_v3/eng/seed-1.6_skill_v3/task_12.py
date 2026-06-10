from ase import Atoms
from ase.build import bulk

a = 2.95
c = a * 1.59
ti_hcp = bulk('Ti', 'hcp', a=a, c=c)

print(ti_hcp.get_cell())
print(ti_hcp.get_positions())
