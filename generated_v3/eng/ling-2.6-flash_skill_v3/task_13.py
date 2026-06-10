from ase import Atoms
from ase.build import bulk

si = bulk('Si', 'diamond', a=5.43)
supercell = si.repeat((3, 3, 3))
print('Number of atoms:', len(supercell))
print('Cell volume:', supercell.get_volume())
