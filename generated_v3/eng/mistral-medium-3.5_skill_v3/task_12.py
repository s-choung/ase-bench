from ase.build import bulk
from ase.calculators.emt import EMT

atoms = bulk('Ti', 'hcp', a=2.95, c=2.95*1.59)
print("Cell vectors:\n", atoms.cell)
print("Atomic positions:\n", atoms.positions)
