from ase.build import mx2
from ase import Atoms

atoms = mx2(formula='MoS2', kind='2H', a=3.16, c=12.294, vacuum=10, orthogonal=True)
print(atoms.cell.cellpar())
