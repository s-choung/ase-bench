from ase.spacegroup import crystal
from ase.io import read, write

# Create NaCl bulk crystal (spacegroup 225 = Fm-3m, experimental lattice constant 5.64 Å)
nacl = crystal(
    symbols=['Na', 'Cl'],
    basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
    spacegroup=225,
    cellpar=[5.64, 5.64, 5.64, 90, 90, 90]
)

# Save to CIF format
write('nacl.cif', nacl, format='cif')

# Read CIF back
read_nacl = read('nacl.cif')

# Extract and print required information
spacegroup = read_nacl.get_spacegroup()
print(f"Spacegroup: {spacegroup}")
print(f"Number of atoms in unit cell: {len(read_nacl)}")
