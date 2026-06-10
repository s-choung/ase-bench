from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc', a=4.08, cubic=True)
write('au_bulk.xyz', atoms, format='xyz')

atoms_read = read('au_bulk.xyz', format='xyz')

for sym, pos in zip(atoms_read.get_chemical_symbols(), atoms_read.get_positions()):
    print(f"{sym}: {pos}")
