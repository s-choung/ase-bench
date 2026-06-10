from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc', a=4.08, cubic=True)

filename = 'au_fcc.xyz'
write(filename, atoms)

atoms2 = read(filename)

for symbol, pos in zip(atoms2.get_chemical_symbols(), atoms2.get_positions()):
    print(symbol, pos)
