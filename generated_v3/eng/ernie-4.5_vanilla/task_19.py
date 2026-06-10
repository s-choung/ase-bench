from ase import Atoms
import numpy as np

# Create CO2 molecule: C at the origin, O atoms at ±1.16 Å along the z-axis
co2 = Atoms('CO2', positions=[(0, 0, 0), (0, 0, 1.16), (0, 0, -1.16)], cell=[10, 10, 10], pbc=False)

# Calculator not necessary for distance calculation, but if required for demonstration:
# from ase.calculators.emt import EMT
# co2.set_calculator(EMT())  # EMT or any other built-in calculator can be used, but not required here

# Calculate and print interatomic distances
distances = co2.get_distances(micro=False)  # Get all pairwise distances

# Print the distances for each pair (excluding self-distances)
print("Interatomic distances (Å):")
for i, d in enumerate(distances[0]):  # Focus on the first atom's connections (C to O)
    if i > 0:  # Exclude self-distance
        print(f"C to O{i} distance: {d:.4f} Å")

# For completeness, print O-O distance
print(f"O1 to O2 distance: {distances[1][2]:.4f} Å")
