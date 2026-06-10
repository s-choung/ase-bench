from ase.build import bcc110

slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)
print(f'Number of atoms: {len(slab)}')
print(f'Cell parameters (a, b, c, α, β, γ): {slab.get_cell_lengths_and_angles()}')
