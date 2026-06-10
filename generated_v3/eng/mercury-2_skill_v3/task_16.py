from ase.build import bcc110

# BCC Fe(110) slab, 2×2 in‑plane, 4 layers, 10 Å vacuum
slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

print('Number of atoms:', slab.get_number_of_atoms())
print('Cell (a, b, c, α, β, γ):', slab.get_cell_lengths_and_angles())
