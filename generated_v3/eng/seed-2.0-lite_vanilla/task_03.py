from ase.build import mx2, add_vacuum

# Create 2H MoS2 monolayer
mos2 = mx2('MoS2')
# Add 10 Å out-of-plane vacuum
add_vacuum(mos2, 10.0)
# Extract and print cell dimensions (Angstrom)
a, b, c = mos2.cell.lengths()
print(f"MoS2 monolayer cell dimensions (Å):\na={a:.2f}, b={b:.2f}, c={c:.2f}")
