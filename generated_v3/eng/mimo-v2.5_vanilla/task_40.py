from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import get_spacegroup

# Create NaCl in rock salt structure
nacl = bulk('NaCl', 'rocksalt', a=6.24)

# Save to CIF
write('NaCl.cif', nacl)

# Read back from CIF
nacl_read = read('NaCl.cif')

# Get space group info
spg = get_spacegroup(nacl_read)

print(f"Space group: {spg}")
print(f"Number of atoms: {len(nacl_read)}")
