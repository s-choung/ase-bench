from ase.build import bulk
from ase import Atoms
import numpy as np

# HCP Ti 구조 생성
a = 2.95
c = a * 1.59
atoms = bulk('Ti', 'hcp', a=a, c=c)

print("Cell vectors:")
print(atoms.get_cell())
print("\nAtomic positions:")
print(atoms.get_positions())
print("\nSymbols:")
print(atoms.get_chemical_symbols())
print("\nCell parameters [a, b, c, α, β, γ]:")
print(atoms.get_cell_lengths_and_angles())
