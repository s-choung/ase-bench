from ase.build import bulk
from ase.io import read, write

# Generate Au FCC bulk structure
au_bulk = bulk('Au', 'fcc', a=4.078, cubic=True)

# Save to XYZ file
write('au_fcc_bulk.xyz', au_bulk)

# Read the saved XYZ file back
read_atoms = read('au_fcc_bulk.xyz')

# Extract and print atom data
atom_types = read_atoms.get_chemical_symbols()
positions = read_atoms.get_positions()

print("Atom types:", atom_types)
print("\nAtomic positions (in Å):")
for sym, pos in zip(atom_types, positions):
    print(f"{sym}: {pos[0]:.3f}, {pos[1]:.3f}, {pos[2]:.3f}")
