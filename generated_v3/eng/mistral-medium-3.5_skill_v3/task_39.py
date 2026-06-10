from ase import Atoms
from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc', a=4.0)
write('au_bulk.xyz', atoms)
atoms_loaded = read('au_bulk.xyz')

print('Atom types:', atoms_loaded.get_chemical_symbols())
print('Positions:', atoms_loaded.get_positions())
