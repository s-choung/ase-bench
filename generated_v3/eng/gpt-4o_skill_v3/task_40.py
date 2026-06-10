from ase.spacegroup import crystal
from ase.io import write, read

# Create NaCl crystal
nacl = crystal('NaCl', [(0, 0, 0), (0.5, 0.5, 0.5)], spacegroup=225, cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

# Save to CIF format
write('nacl.cif', nacl, format='cif')

# Read from CIF file
nacl_read = read('nacl.cif', format='cif')

# Print spacegroup and number of atoms
print(f"Spacegroup: {nacl_read.get_spacegroup().symbol}")
print(f"Number of atoms: {len(nacl_read)}")
