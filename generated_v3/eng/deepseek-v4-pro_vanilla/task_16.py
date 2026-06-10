from ase.build import bcc110

atoms = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)
print('Number of atoms:', len(atoms))
print('Cell size:', atoms.cell.lengths())
