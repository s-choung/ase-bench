from ase import Atoms
from ase.geometry import get_distances

# Create CO2 molecule: C at origin, O atoms at +/- 1.16A on x-axis
atoms = Atoms('CO2', 
              positions=[(0, 0, 0), (1.16, 0, 0), (-1.16, 0, 0)], 
              cell=(10, 10, 10), 
              pbc=False)

# Calculate distances between all pairs
dist_matrix = get_distances(atoms, atoms)

print("Interatomic distance matrix:\n", dist_matrix)
