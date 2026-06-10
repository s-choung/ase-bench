from ase.build import bulk
from ase.io import read, write
from ase.spacegroup import get_spacegroup

# Create NaCl crystal structure
nacl = bulk('NaCl', 'rocksalt', a=5.64)

# Save to CIF format
write('nacl.cif', nacl)

# Read back from CIF
nacl_read = read('nacl.cif')

# Get spacegroup information
sg = get_spacegroup(nacl_read)

# Print results
print(f"Spacegroup: {sg.symbol} ({sg.no})")
print(f"Number of atoms: {len(nacl_read)}")
