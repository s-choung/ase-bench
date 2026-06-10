from ase.build import bulk
from ase.io import write, read

au_bulk = bulk('Au', 'fcc')
write('au_fcc.xyz', au_bulk)

au_read = read('au_fcc.xyz')
print("Atom types:", au_read.get_chemical_symbols())
print("Positions:\n", au_read.get_positions())
