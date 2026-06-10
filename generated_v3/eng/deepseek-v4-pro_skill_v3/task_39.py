from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc')
write('au.xyz', atoms)
atoms_in = read('au.xyz')
print('Symbols:', atoms_in.get_chemical_symbols())
print('Positions:', atoms_in.get_positions())
