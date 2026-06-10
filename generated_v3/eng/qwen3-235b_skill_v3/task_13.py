from ase.build import bulk
from ase import units

si_bulk = bulk('Si', 'diamond', a=5.43)
si_supercell = si_bulk * (3, 3, 3)

print(len(si_supercell))
print(si_supercell.get_volume())
