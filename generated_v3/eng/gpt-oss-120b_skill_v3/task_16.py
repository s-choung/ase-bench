from ase.build import bcc110
from ase import units

# BCC Fe (110) surface: 2×2 in‑plane, 4 atomic layers, 10 Å vacuum
slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0, a=2.866)  # a in Å for Fe

print('Number of atoms :', slab.get_number_of_atoms())

# cell lengths (Å) and angles (deg): a, b, c, α, β, γ
a, b, c, alpha, beta, gamma = slab.get_cell_lengths_and_angles()
print(f'Cell lengths  : a={a:.3f} Å  b={b:.3f} Å  c={c:.3f} Å')
print(f'Cell angles   : α={alpha:.1f}°  β={beta:.1f}°  γ={gamma:.1f}°')
