from ase import Atoms

# Create CO2 molecule
atoms = Atoms('CO2', positions=[(0,0,0), (1.16,0,0), (-1.16,0,0)])

# Set unit cell (non‑periodic)
atoms.set_cell([10, 10, 10])

# Calculate distances
dist = atoms.get_distances(0, [1, 2])
print("C‑O1 distance (Å):", dist[0][0])
print("C‑O2 distance (Å):", dist[1][0])
