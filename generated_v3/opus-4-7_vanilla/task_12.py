from ase.build import bulk
import numpy as np

a = 2.95
c = a * 1.59
ti = bulk('Ti', 'hcp', a=a, c=c)

print("Cell vectors:")
print(np.array(ti.cell))
print("\nAtomic positions:")
print(ti.get_positions())
print("\nChemical symbols:", ti.get_chemical_symbols())
