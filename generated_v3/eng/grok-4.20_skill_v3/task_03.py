from ase.build import mx2
from ase import units
import numpy as np

atoms = mx2('MoS2', kind='2H', a=3.18, thickness=3.17, vacuum=10.0)
print(atoms.get_cell_lengths_and_angles()[:3])
