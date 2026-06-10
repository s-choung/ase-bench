from ase import Atoms
from ase.build import surface

# Build 100 Cu surface
Cu_surface = surface('Cu', (1, 0, 0), size=(3, 3, 3), layers=3, vacuum=12.0, orthorhombic=True)

# Print basic information
print(f"Number of atoms: {len(Cu_surface)}")
print(f"Cell vectors (Angstrom):", Cu_surface.cell)
print(f"Cartesian coordinates:", Cu_surface.get_positions())
