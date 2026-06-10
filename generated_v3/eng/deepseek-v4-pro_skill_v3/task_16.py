from ase.build import bcc110

# Create Fe BCC(110) surface: 2x2x4, vacuum=10 Å
atoms = bcc110('Fe', size=(2, 2, 4), vacuum=10)

# Print number of atoms and cell dimensions
print('Number of atoms:', len(atoms))
cell_pars = atoms.get_cell_lengths_and_angles()
print(f'Cell lengths (Å): {cell_pars[0]:.3f}, {cell_pars[1]:.3f}, {cell_pars[2]:.3f}')
print(f'Cell angles (°): {cell_pars[3]:.1f}, {cell_pars[4]:.1f}, {cell_pars[5]:.1f}')
