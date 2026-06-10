from ase.build import nanotube
from ase.lattice.hexagonal import Graphite

nt = nanotube(6, 6, length=4, atom=Graphite())
print('Number of atoms:', len(nt))
print('Cell:', nt.cell)
