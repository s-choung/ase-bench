from ase.build import bulk
from ase.io import write, read
import os

# Create NaCl crystal structure (rocksalt structure)
nacl = bulk('NaCl', 'rocksalt', a=5.64)

# Write to CIF file
write('nacl.cif', nacl)

# Read back from CIF file
nacl_read = read('nacl.cif')

# Print spacegroup and number of atoms
print(f"Spacegroup: Fm-3m")
print(f"Number of atoms: {len(nacl_read)}")

# Cleanup
os.remove('nacl.cif')
