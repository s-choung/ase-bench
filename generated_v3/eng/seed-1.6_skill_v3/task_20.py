from ase.build import nanotube

nt = nanotube(6, 6, length=4, symbol='C')
print(f'Number of atoms: {len(nt)}')
print('Cell info (a, b, c, α, β, γ):', nt.get_cell_lengths_and_angles())
