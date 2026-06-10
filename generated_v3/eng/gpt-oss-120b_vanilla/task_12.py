from ase.build import bulk
from ase.calculators.emt import EMT

a = 2.95
c = a * 1.59
ti = bulk('Ti', 'hcp', a=a, c=c)
ti.calc = EMT()

print("Cell vectors (Å):")
print(ti.get_cell())

print("\nAtomic positions (Å):")
print(ti.get_positions())
