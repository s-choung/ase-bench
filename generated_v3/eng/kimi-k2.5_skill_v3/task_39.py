from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc', a=4.078, cubic=True)
write('au.xyz', atoms)
atoms = read('au.xyz')
print(atoms.get_chemical_symbols())
print(atoms.get_positions())
