from ase.build import bulk
from ase.io import write

a = 2.95
c = a * 1.59
atoms = bulk('Ti', crystalstructure='hcp', a=a, c=c)

print("Cell vectors:")
for vec in atoms.cell:
    print(vec)
print("\nAtomic positions (fractional):")
for pos in atoms.get_scaled_positions():
    print(pos)
print("\nAtomic positions (Cartesian):")
for pos in atoms.positions:
    print(pos)
