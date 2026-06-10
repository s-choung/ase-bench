from ase import Atoms
from ase.build import bulk, slab
import numpy as np

# Create MoS2 monolayer
atoms = bulk('MoS2', 'hexagonal', a=3.18, c=1.85)
atoms = slab(atoms, thickness=1, direction=(1, 1, 0))

# Add 10 Å vacuum in z-direction
atoms.cell[2] += 10.0

# Print cell size
print(atoms.cell)
