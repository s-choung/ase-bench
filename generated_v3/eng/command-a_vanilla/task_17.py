from ase.build import surface
from ase.visualize import view

# Create Cu (111) surface with 3 layers and 10 angstroms of vacuum
cu_surface = surface('Cu', (2, 1, 1), layers=3, vacuum=10.0)

# Print number of atoms and cell parameters
print(f"Number of atoms: {len(cu_surface)}")
print(f"Cell: {cu_surface.cell}")
