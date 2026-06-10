from ase.spacegroup import crystal
from ase.io import write, read

# Create NaCl crystal structure
nacl = crystal('NaCl', [(0, 0, 0), (0.5, 0.5, 0.5)], spacegroup=225, cellpar=[4.1, 4.1, 4.1, 90, 90, 90])

# Save to CIF file
write('nacl.cif', nacl, format='cif')

# Read CIF file
nacl_read = read('nacl.cif', format='cif')

# Print spacegroup information and number of atoms
print(f"Spacegroup: {nacl_read.get_spacegroup().no}, {nacl_read.get_spacegroup().symbol}")
print(f"Number of atoms: {len(nacl_read)}")
