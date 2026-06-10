from ase.build import bulk, surface, molecule

# Create Al(111) 3-layer slab with 10 A vacuum
al = bulk('Al', 'fcc', a=4.05)
slab = surface(al, (1, 1, 1), 3, vacuum=10)

# Identify top layer atoms for adsorption site
positions = slab.get_positions()
z = positions[:, 2]
top_z = max(z)
top_indices = [i for i, zi in enumerate(z) if abs(zi - top_z) < 1e-5]

# Calculate bridge site coordinates
pos1 = positions[top_indices[0]]
pos2 = positions[top_indices[1]]
bridge = (pos1 + pos2) / 2.0
bridge[2] += 2.0  # Add 2.0 A height

# Add N2 molecule
n2 = molecule('N2')
n2.translate(bridge)

# Combine slab and molecule
final = slab + n2

# Output results
print(len(final))
print(final.get_chemical_symbols())
