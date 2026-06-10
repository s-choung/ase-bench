from ase.build import surface
from ase.build import bulk
from ase.io import write

# Create a copper bulk
cu_bulk = bulk('Cu', 'fcc', a=3.61, cubic=True)

# Cut the (2,1,1) surface
cu_surface = surface(cu_bulk, (2, 1, 1), 3, vacuum=10.0)

# Print the number of atoms and cell
print("Number of atoms:", len(cu_surface))
print("Cell:", cu_surface.cell)

# Optional: Save the structure to a file
write('cu_surface.xyz', cu_surface)
