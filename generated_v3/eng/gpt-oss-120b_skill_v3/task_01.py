from ase.build import bulk

# Cu FCC bulk
cu = bulk('Cu', 'fcc', a=3.6)

# 2x2x2 supercell
supercell = cu * (2, 2, 2)   # or cu.repeat((2,2,2))

# Cell info: a, b, c, α, β, γ
cell_info = supercell.get_cell_lengths_and_angles()
print(f'Cell lengths (Å): a={cell_info[0]:.3f}, b={cell_info[1]:.3f}, c={cell_info[2]:.3f}')
print(f'Cell angles (deg): α={cell_info[3]:.1f}, β={cell_info[4]:.1f}, γ={cell_info[5]:.1f}')
print('Number of atoms:', len(supercell))
