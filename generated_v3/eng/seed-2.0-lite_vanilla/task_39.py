from ase.build import bulk
from ase.io import read, write

# Create FCC gold bulk conventional cubic cell
au_bulk = bulk('Au', 'fcc', a=4.08, cubic=True)

# Save to XYZ file
write('au_fcc_bulk.xyz', au_bulk)

# Read back from XYZ
read_atoms = read('au_fcc_bulk.xyz')

# Print atom types and positions
print("Atom types and Cartesian positions (Angstrom):")
for symbol, pos in zip(read_atoms.get_chemical_symbols(), read_atoms.get_positions()):
    print(f"{symbol}: {pos.round(4)}")
