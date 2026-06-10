from ase.build import fcc100

# Create Cu(100) surface
surface = fcc100('Cu', size=(3,3,3), vacuum=12)

# Print number of atoms
print(f"Number of atoms: {len(surface)}")

# Print cell info (a, b, c, α, β, γ)
cell_info = surface.cell.array
a, b, c, alpha, beta, gamma = surface.cell.lengths_and_angles()
print(f"Cell lengths: a={a:.1f} Å, b={b:.1f} Å, c={c:.1f} Å")
print(f"Cell angles: α={alpha:.1f}°, β={beta:.1f}°, γ={gamma:.1f}°")
