from ase import Atoms
from ase.build import surface

# Create Cu(100) surface
cu = surface('Cu', (3, 3), (0, 0, 1), cellparam=3.615, pbc=(1, 1, 0))

# Add vacuum layer
cu.cell += (0, 0, 12)

# Print cell information and number of atoms
print("Cell:", cu.cell)
print("Number of atoms:", len(cu))
