from ase import Atoms
from ase.build import bulk, surface
from ase.calculators.emt import EMT

# Create Cu bulk crystal
cu_bulk = bulk('Cu', 'fcc', a=3.615)

# Define Miller indices and number of surface layers
miller_indices = (2, 1, 1)
num_layers = 3

# Create the surface with vacuum
cu_surface = surface(cu_bulk, miller_indices, layers=num_layers, vacuum=10)

# Print the number of atoms and cell parameters
print("Number of atoms:", len(cu_surface))
print("Cell:\n", cu_surface.cell)
