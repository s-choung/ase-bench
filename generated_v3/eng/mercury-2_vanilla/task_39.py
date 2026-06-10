from ase.build import bulk
from ase.io import write, read

# Create FCC Au bulk
atoms = bulk('Au', 'fcc', a=4.08, cubic=True)

# Save to XYZ and read back
write('au_bulk.xyz', atoms)
atoms2 = read('au_bulk.xyz')

# Print element symbols and positions
for sym, pos in zip(atoms2.get_chemical_symbols(), atoms2.positions):
    print(sym, pos)
