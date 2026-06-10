from ase.build import bulk

cu_bulk = bulk('Cu', 'fcc', a=3.6)
supercell = cu_bulk * (2, 2, 2)
cell_params = supercell.get_cell_lengths_and_angles()
print(f"Cell parameters: a={cell_params[0]:.2f} Å, b={cell_params[1]:.2f} Å, c={cell_params[2]:.2f} Å, α={cell_params[3]:.2f}°, β={cell_params[4]:.2f}°, γ={cell_params[5]:.2f}°")
print(f"Number of atoms: {len(supercell)}")
