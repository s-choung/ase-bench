from ase.build import bulk
import numpy as np

atoms = bulk('Ti', 'hcp', a=2.95, c_over_a=1.59)

print("Cell vectors:")
print(atoms.cell)

print("\nAtomic positions:")
for pos in atoms.get_positions():
    print(pos)
