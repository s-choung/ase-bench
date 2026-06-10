from ase.build import mx2, add_vacuum

# Create standard 2H-phase MoS2 monolayer
mos2 = mx2('MoS2', kind='2H')
# Add 10 Å out-of-plane (z-direction) vacuum
add_vacuum(mos2, 10.0)
# Extract and print cell dimensions
a, b, c, *_ = mos2.get_cell_lengths_and_angles()
print(f"Unit cell sizes (Å): a={a:.3f}, b={b:.3f}, c={c:.3f}")
print("\nFull unit cell matrix (Å):\n", mos2.get_cell())
