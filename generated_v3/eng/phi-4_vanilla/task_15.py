from ase.build import bulk, cut
from ase.io import write

# Create cubic copper bulk structure
cu_bulk = bulk('Cu', 'fcc')

# Cut the bulk to create a 3-layer Cu(100) surface with specified size and vacuum
cu_surface = cut(cu_bulk, (100, 0, 0), size=(3, 3, 3), vacuum=12.0)

# Print the number of atoms and cell info
print(len(cu_surface), cu_surface.get_cell())

# Optionally, save the structure to a file
write('cu_surface.xyz', cu_surface)
