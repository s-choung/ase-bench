from ase.build import nanotube

# (6,6) armchair CNT, length ≈ 4 Å
cnt = nanotube(6, 6, length=4.0)

print("Number of atoms :", len(cnt))
# cell lengths (a, b, c) in Å and angles (α, β, γ) in degrees
a, b, c, alpha, beta, gamma = cnt.get_cell_lengths_and_angles()
print(f"Cell lengths  : a={a:.3f} Å  b={b:.3f} Å  c={c:.3f} Å")
print(f"Cell angles   : α={alpha:.1f}°  β={beta:.1f}°  γ={gamma:.1f}°")
