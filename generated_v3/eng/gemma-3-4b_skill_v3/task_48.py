from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.geometry import get_distances
from ase.lattice import Slab
import numpy as np
from ase.visualize import view

# Create a Cu bulk
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True, orthorhombic=True)

# Create a 2x2x2 slab
slab = Slab(atoms, соотношение=2, height=4, size=(2, 2, 4), symmetry='cubic')

# Set the calculator
slab.calc = EMT()

# Get the distances between atom 0 and all other atoms
distances = get_distances(slab, mic=True)

# Find the minimum and maximum distances
min_dist = np.min(distances)
max_dist = np.max(distances)

print(f"Minimum distance: {min_dist:.2f} Angstroms")
print(f"Maximum distance: {max_dist:.2f} Angstroms")

#Visualize the structure for a quick check
view(slab)
