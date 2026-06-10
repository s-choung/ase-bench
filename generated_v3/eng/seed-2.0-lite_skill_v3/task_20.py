from ase.build import nanotube

# Create (6,6) carbon nanotube with length 4
cnt = nanotube(6, 6, length=4, symbol='C')

# Print number of atoms
print(f"Total number of atoms: {len(cnt)}")

# Print cell information (a,b,c in Å, α,β,γ in degrees)
cell_params = cnt.get_cell_lengths_and_angles()
a, b, c, alpha, beta, gamma = cell_params
print(f"\nCell information:")
print(f"Lattice lengths (Å): a={a:.3f}, b={b:.3f}, c={c:.3f}")
print(f"Lattice angles (°): α={alpha:.1f}, β={beta:.1f}, γ={gamma:.1f}")
