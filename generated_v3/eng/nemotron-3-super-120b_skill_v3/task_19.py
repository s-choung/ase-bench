from ase import Atoms

# Create CO2: C at origin, O atoms ±1.16 Å along z
atoms = Atoms('COO', positions=[
    [0.0, 0.0, 0.0],          # C
    [0.0, 0.0, 1.16],         # O1
    [0.0, 0.0, -1.16]         # O2
])

# Set cubic cell 10 Å and turn off periodic boundary conditions
atoms.set_cell([10.0, 10.0, 10.0])
atoms.set_pbc(False)

# Compute and print all interatomic distances
dist_matrix = atoms.get_all_distances(mic=False)
print("Distance matrix (Å):")
print(dist_matrix)
