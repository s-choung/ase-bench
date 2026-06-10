from ase import Atoms
from ase.visualize import view
from ase.build import mx2

# Create MoS2 monolayer with 3x3 unit cells
mos2 = mx2(a=3.18, thickness=3.15, formula='MoS2', kind='2H', lattice='hexagonal', layers=1, vacuum=10.0)

# Print cell size
print(mos2.cell.lengths())
