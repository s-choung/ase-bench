from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc', a=4.078)

write('au_fcc.xyz', atoms)

atoms2 = read('au_fcc.xyz')

for s, p in zip(atoms2.get_chemical_symbols(), atoms2.get_positions()):
    print(s, p)
