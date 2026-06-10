from ase.build import bulk
from ase.io import read, write

atoms = bulk('Au', 'fcc', a=4.08)
write('au_bulk.xyz', atoms)

atoms_read = read('au_bulk.xyz')

print("Atom types:", atoms_read.get_chemical_symbols())
print("Positions (Å):")
for pos in atoms_read.get_positions():
    print(f"  {pos}")
