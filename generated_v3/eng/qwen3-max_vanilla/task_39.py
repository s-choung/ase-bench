from ase.build import bulk
from ase.io import read, write

# Create and save Au FCC bulk
au = bulk('Au', 'fcc', a=4.08)
write('au_fcc.xyz', au)

# Read back and print atom types and positions
atoms = read('au_fcc.xyz')
print('Atom types:', atoms.get_chemical_symbols())
print('Positions:\n', atoms.get_positions())
