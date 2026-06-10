from ase.io import read, write
from ase.build import bulk

atoms = bulk('Au', 'fcc', a=4.078)
write('Au.xyz', atoms)
atoms = read('Au.xyz')
print(atoms.get_chemical_symbols())
print(atoms.positions)
