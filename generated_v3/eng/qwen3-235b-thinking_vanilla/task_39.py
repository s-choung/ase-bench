from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc', cubic=True)
write('au_bulk.xyz', atoms)
atoms_reloaded = read('au_bulk.xyz')
print(atoms_reloaded.get_chemical_symbols())
print(atoms_reloaded.get_positions())
