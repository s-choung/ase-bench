from ase.build import bcc110

atoms = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)
print(f'Number of atoms: {len(atoms)}')
print(f'Cell:\n{atoms.cell}')
print(f'Cell lengths: {atoms.cell.lengths()}')
