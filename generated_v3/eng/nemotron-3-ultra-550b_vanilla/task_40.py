from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import get_spacegroup

# Create NaCl structure (rocksalt)
nacl = bulk('NaCl', 'rocksalt', a=5.64)

# Save to CIF
write('nacl.cif', nacl)

# Read back
nacl_read = read('nacl.cif')

# Spacegroup info
spg = get_spacegroup(nacl_read)
print(f"Spacegroup: {spg.no} ({spg.symbol})")
print(f"Number of atoms: {len(nacl_read)}")
