from ase.build import bulk
from ase.io import read, write
from ase.spacegroup import crystal

# Create NaCl crystal
nacl = bulk('NaCl', 'rocksalt', a=5.64)

# Save to CIF
write('nacl.cif', nacl)

# Read from CIF
nacl_read = read('nacl.cif')

# Print spacegroup and number of atoms
print(f"Spacegroup: {nacl_read.info.get('spacegroup', 'N/A')}")
print(f"Number of atoms: {len(nacl_read)}")
