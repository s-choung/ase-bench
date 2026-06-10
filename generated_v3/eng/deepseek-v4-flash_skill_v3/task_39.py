from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc', a=4.08)
write('au_bulk.xyz', atoms)
read_atoms = read('au_bulk.xyz')
print('Atom types:', read_atoms.get_chemical_symbols())
print('Positions (Å):')
for pos in read_atoms.get_positions():
    print(pos)
