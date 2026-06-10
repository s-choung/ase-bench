from ase.build import bulk, surface
from ase.io import write

# Create Cu bulk and cut (2,1,1) surface with 3 layers
atoms = bulk('Cu', 'fcc', a=3.6)
slab = surface(atoms, (2, 1, 1), layers=3)

# Add 10 Angstroms of vacuum to the z-direction
# Note: surface() creates a slab; add_vacuum is in-place
from ase.build import add_vacuum
add_vacuum(slab, 10.0)

# Print number of atoms and cell
print(f"Number of atoms: {len(slab)}")
print(f"Cell dimensions:\n{slab.get_cell()}")
