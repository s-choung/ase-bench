from ase.build import surface
from ase import Atoms
from ase.calculators.emt import EMT

# Create Cu bulk with lattice parameter ~3.61 Å
cu_bulk = Atoms('Cu', positions=[[0, 0, 0]], cell=[[0, 0.5, 0.5], [0.5, 0, 0.5], [0.5, 0.5, 0]], pbc=True)
cu_bulk *= 4  # Sufficiently large bulk for surface creation

# Cut (2,1,1) surface with 3 layers
slab = surface(cu_bulk, indices=(2,1,1), layers=3)

# Add vacuum (in z-direction)
from ase.build import add_vacuum
add_vacuum(slab, vacuum=10.0)

# Print number of atoms and cell
print("Number of atoms:", len(slab))
print("Cell:", slab.get_cell())
