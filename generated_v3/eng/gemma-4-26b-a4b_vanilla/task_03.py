import numpy as np
from ase.build import mx2
from ase.visualize import view

# Create MoS2 monolayer
# a is lattice constant, thickness is the approximate layer thickness
mols2 = mx2(formula='MoS2', a=3.16, thickness=3.12)

# Add 10 Angstroms of vacuum along the z-axis
mols2.center(vacuum=10.0, axis=2)

# Print cell size
print(f"Cell dimensions (Å):\n{mols2.get_cell()}")
