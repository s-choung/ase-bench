from ase.build import bulk
from ase import Atoms
import numpy as np

atoms = bulk('Ti', 'hcp', a=2.95, c=2.95*1.59)
atoms.calc = None

print("Cell vectors:")
print(atoms.get_cell())
print("\nAtomic positions:")
print(atoms.get_positions())
