from ase.build import bulk
import numpy as np

a = 2.95
covera = 1.59

ti = bulk("Ti", "hcp", a=a, covera=covera)

np.set_printoptions(precision=6, suppress=True)

print("Cell vectors (Angstrom):")
print(ti.cell.array)

print("\nAtomic positions (Angstrom):")
print(ti.get_positions())
