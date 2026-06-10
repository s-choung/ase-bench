from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc', a=4.08)
write('au_fcc.xyz', atoms)

atoms_read = read('au_fcc.xyz')
print(atoms_read.get_chemical_symbols())
print(atoms_read.positions)
