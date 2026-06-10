from ase.build import bulk
from ase.calculators.emt import EMT

a = 2.95
c = a * 1.59

atoms = bulk('Ti', 'hcp', a=a, c=c)
atoms.set_calculator(EMT())

print("Cell vectors:\n", atoms.cell)
print("\nAtomic positions:\n", atoms.get_positions())
