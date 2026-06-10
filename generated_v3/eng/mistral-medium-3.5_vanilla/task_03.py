from ase.lattice.hexagonal import Monolayer
from ase.build import add_vacuum

atoms = Monolayer('MoS2', kind='2H', a=3.19, h=3.12)
add_vacuum(atoms, 10.0)
print(atoms.cell.lengths())
