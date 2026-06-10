from ase.build import surface
from ase.lattice.cubic import FaceCenteredCubic

# Create Cu bulk with FCC structure
cu_bulk = FaceCenteredCubic('Cu', latticeconstant=3.615)

# Cut (2,1,1) surface with 3 layers and 10 Å vacuum
cu_surface = surface(cu_bulk, (2,1,1), layers=3, vacuum=10.0)

# Print results
print(f"Number of atoms: {len(cu_surface)}")
print(f"Cell:\n{cu_surface.get_cell()}")
