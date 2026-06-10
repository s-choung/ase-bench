from ase.build import bulk
from ase import Atoms
import numpy as np

# Diamond silicon (fcc with two atoms per cell)
si = bulk('Si', 'diamond', a=5.43)

# 3x3x3 supercell
si_super = si * (3, 3, 3)

# Print results
print(f'Number of atoms: {len(si_super)}')
print(f'Cell volume (Å³): {si_super.get_volume():.6f}')
