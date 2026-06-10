from ase.build import bulk, surface
from ase import Atoms

# Create a Cu bulk structure
cu_bulk = bulk('Cu', 'fcc')

# Cut a (2,1,1) surface with 3 layers and add 10 Å of vacuum
cu_surface = surface(cu_bulk, (2, 1, 1), layers=3, vacuum=10)

# Print the number of atoms and the cell
print("Number of atoms:", len(cu_surface))
print("Cell dimensions:")
print(cu_surface.cell)
