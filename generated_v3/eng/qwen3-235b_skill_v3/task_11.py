from ase import build

atoms = build.bulk('Al', 'bcc', a=3.3, cubic=True)
print(atoms.get_cell_lengths_and_angles())
print(atoms.symbols)
