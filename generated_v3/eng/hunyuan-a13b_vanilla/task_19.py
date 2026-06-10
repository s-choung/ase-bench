from ase import Atoms

# Create CO2 molecule
co2 = Atoms('O', [(0.0, 0.0, 0.0)], cell=(10, 10, 10), pbc=False)
co2.extend('O', positions=[(1.16, 0.0, 0.0)])
co2菜品tenize()

# Calculate interatomic distances
distances = co2.get_distances()

# Print distances
for pair in distances:
    print(f"Distance between atoms {pair[0]} and {pair[1]}: {pair[2]:.2f} Å")
