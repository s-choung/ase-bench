from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc', a=4.08, cubic=True)
write('au_fcc.xyz', atoms)

atoms2 = read('au_fcc.xyz')
print(atoms2.get_chemical_symbols())
print(atoms2.get_positions())
