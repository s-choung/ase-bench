from ase.build import mx2
from ase.calculators.emt import EMT

atoms = mx2('MoS2', kind='2H', vacuum=10)
print("Cell size (a, b, c):", atoms.cell.lengths())
