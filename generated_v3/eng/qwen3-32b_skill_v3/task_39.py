from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc', a=4.08)
write('au_bulk.xyz', atoms)
atoms_read = read('au_bulk.xyz')

for symbol, pos in zip(atoms_read.get_chemical_symbols(), atoms_read.get_positions()):
    print(f"{symbol} {pos}")
