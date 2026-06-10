from ase.spacegroup import crystal
from ase.io import read, write

# Create NaCl rock-salt structure (spacegroup 225, Fm-3m)
nacl = crystal(['Na', 'Cl'], basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
               spacegroup=225, cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

# Save as CIF
write('NaCl.cif', nacl)

# Read back
nacl_read = read('NaCl.cif')

# Print spacegroup and atom count
print(f"Spacegroup: {nacl_read.get_spacegroup().no} ({nacl_read.get_spacegroup().symbol})")
print(f"Number of atoms: {len(nacl_read)}")
