from ase.build import bcc110

# Fe BCC(110) surface: 2x2 in-plane, 4 layers, 10 Å vacuum
atoms = bcc110('Fe', size=(2, 2, 4), vacuum=10)

print('Number of atoms:', len(atoms))
print('Cell (Å):')
print(atoms.get_cell())
