import numpy as np
from ase.build import bulk
from ase.geometry import get_distances

# Create a Cu FCC bulk 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))

# Calculate distances from atom 0 to all other atoms (1 to N-1)
# mic=True accounts for periodic boundary conditions
distances = get_distances(atoms, 0, slice(1, atoms.get_number_of_atoms()), mic=True)

# Output results
print(f"Minimum distance: {np.min(distances):.4f} Å")
print(f"Maximum distance: {np.max(distances):.4f} Å")
