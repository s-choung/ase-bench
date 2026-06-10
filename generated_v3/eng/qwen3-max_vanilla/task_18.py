from ase import db
from ase.data.g2 import data

# Retrieve CH4 from ASE G2 database
atoms = data['CH4']

# Print chemical formula
print("Chemical formula:", atoms.get_chemical_formula())

# Print atomic coordinates
print("Atomic coordinates (Å):")
print(atoms.positions)

# Print bond lengths (C-H bonds)
from ase.geometry import get_distances
distances = get_distances(atoms.positions, atoms.positions)[1][0]  # distance matrix
# CH4 has 4 H atoms (indices 1-4) bonded to C (index 0)
for i in range(1, 5):
    print(f"C-H bond length (Å): {distances[i]:.4f}")
