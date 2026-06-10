from ase import Atoms
from ase.build import mx2
from ase.units import Ang

# Create MoS2 monolayer (2H phase)
atoms = mx2('MoS2', kind='2H', a=3.18, thickness=3.17, vacuum=0.0)

# Add 10 Å vacuum (in-place modification)
from ase.build import add_vacuum  # Actually we can do it directly via function call (as per earlier note) but the import is consistent with doc
# Alternatively, the function can be called as below (the build module hasfunctions to modify in-place)
# However, note that the 'mx2' already creates a slab, so we use add_vacuum
add_vacuum(atoms, 10.0)  # Modifies atoms in-place

# Alternative: if we want to avoid in-place modification for clarity (though the doc says in-place is the way),
# we can recreate (but the function is designed for in-place). So we stick with in-place.

# Print cell size (a, b, c lengths and angles)
cell_params = atoms.get_cell_lengths_and_angles()
print(f"Cell parameters (a, b, c, alpha, beta, gamma): {cell_params}")

# If you want just the cell vectors (as a 3x3 array):
cell_vectors = atoms.get_cell()
print(f"Cell vectors (Ang):\n{cell_vectors}")
