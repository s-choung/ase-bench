from ase.build import bulk
import numpy as np

a = 2.95
c_over_a = 1.59
c = a * c_over_a

atoms = bulk('Ti', 'hcp', a=a, c=c)

print("Cell vectors (Angstrom):")
for vector in atoms.get_cell():
    print(vector)

print("\nAtomic positions (Angstrom):")
for position in atoms.get_positions():
    print(position)
