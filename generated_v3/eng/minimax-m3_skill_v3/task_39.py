from ase.build import bulk
from ase.io import read, write

atoms = bulk('Au', 'fcc', a=4.08)
write('au_bulk.xyz', atoms)
atoms_read = read('au_bulk.xyz')

print("Symbols:", atoms_read.get_chemical_symbols())
print("Positions:")
for sym, pos in zip(atoms_read.get_chemical_symbols(), atoms_read.get_positions()):
    print(f"  {sym}: {pos}")
