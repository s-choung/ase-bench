from ase.build import bulk
from ase.io import write, read

write('au_bulk.xyz', bulk('Au'))
atoms = read('au_bulk.xyz')

print("Atom types:", atoms.get_chemical_symbols())
print("Positions:\n", atoms.get_positions())
