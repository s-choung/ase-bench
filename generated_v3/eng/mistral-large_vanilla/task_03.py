from ase.build import mx2
from ase import Atoms

mos2 = mx2(formula='MoS2', kind='2H', a=3.18, thickness=3.19)
mos2.center(vacuum=10, axis=2)
print("Cell size:", mos2.cell.cellpar())
