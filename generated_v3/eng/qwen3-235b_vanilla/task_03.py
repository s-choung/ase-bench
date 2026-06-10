from ase import Atoms
from ase.build import surface
from ase.visualize import view

# Create MoS2 monolayer using 2H phase parameters
a = 3.18  # lattice constant in angstrom
c = 10.0  # include vacuum

# Define unit cell
mos2 = surface('MoS2', indices=(0, 0, 1), layers=3, vacuum=10, primitive=1)
mos2.center(vacuum=10, axis=2)

# Print cell size
print(mos2.get_cell())
