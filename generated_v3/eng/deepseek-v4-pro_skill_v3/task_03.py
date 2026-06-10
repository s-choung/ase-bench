from ase.build import mx2, add_vacuum

# Create MoS2 monolayer with typical lattice parameters
mos2 = mx2(formula='MoS2', kind='2H', a=3.18, thickness=3.17)

# Add 10 Å of vacuum in the z-direction (non-periodic in z, but vacuum separates periodic images)
add_vacuum(mos2, 10.0)

# Print the cell vectors (cell size)
print("Cell vectors (Å):")
print(mos2.cell)

# Alternatively, print cell lengths and angles
a, b, c, alpha, beta, gamma = mos2.get_cell_lengths_and_angles()
print(f"\nCell lengths: a={a:.2f}, b={b:.2f}, c={c:.2f} Å")
print(f"Angles: α={alpha:.2f}°, β={beta:.2f}°, γ={gamma:.2f}°")
