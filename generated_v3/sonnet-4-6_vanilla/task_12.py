from ase.build import bulk
from ase import Atoms
import numpy as np

a = 2.95
c = a * 1.59

ti_hcp = bulk('Ti', crystalstructure='hcp', a=a, c=c)

print("Cell vectors:")
print(ti_hcp.cell[:])
print("\nAtom positions:")
for atom in ti_hcp:
    print(f"  {atom.symbol}: {atom.position}")
print(f"\na = {a} Å, c = {c:.4f} Å, c/a = {c/a:.2f}")
print(f"Number of atoms: {len(ti_hcp)}")
