from ase.build import bulk

# Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)

# 2×2×2 supercell
atoms = atoms * (2, 2, 2)

# Cell parameters
a, b, c, alpha, beta, gamma = atoms.get_cell_lengths_and_angles()
print(f"a = {a:.3f} Å, b = {b:.3f} Å, c = {c:.3f} Å")
print(f"α = {alpha:.2f}°, β = {beta:.2f}°, γ = {gamma:.2f}°")

# Number of atoms
print("Number of atoms:", len(atoms))
