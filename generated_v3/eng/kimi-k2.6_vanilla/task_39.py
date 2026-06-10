from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc')
write('Au_bulk.xyz', atoms)
atoms = read('Au_bulk.xyz')

print(atoms.get_chemical_symbols())
print(atoms.positions)
