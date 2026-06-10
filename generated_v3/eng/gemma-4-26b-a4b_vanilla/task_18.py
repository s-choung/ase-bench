from ase.db import connect
from ase.geometry import get_distances

# Connect to the ASE G2 database and retrieve CH4
db = connect('ase/g2.db')
molecule = db.get_by(formula='CH4')

# Print Chemical Formula
print(f"Formula: {molecule.get_chemical_formula()}")

# Print Atomic Coordinates
print("Atomic Coordinates:")
print(molecule.get_positions())

# Calculate and print bond lengths (distance from C (index 0) to all H (indices 1-4))
distances = get_distances(molecule.positions[0:1], molecule.positions[1:5], mic=True)
print("\nBond Lengths (C-H):")
for d in distances.flatten():
    print(f"{d:.4f} Å")
