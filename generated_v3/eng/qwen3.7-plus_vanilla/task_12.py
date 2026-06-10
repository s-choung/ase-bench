from ase.build import bulk
from ase.calculators.emt import EMT

a = 2.95
atoms = bulk('Ti', 'hcp', a=a, c=a * 1.59)
atoms.calc = EMT()

print("Cell vectors:\n", atoms.cell)
print("Atomic positions:\n", atoms.positions)
