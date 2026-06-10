from ase import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc', a=4.08)
write('au_bulk.xyz', atoms)
atoms_read = read('au_bulk.xyz')
print(atoms_read.get_chemical_symbols())
print(atoms_read.get_positions())
