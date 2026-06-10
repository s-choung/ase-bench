from ase import Atoms
from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import get_spacegroup

# Create NaCl crystal structure
nacl = bulk('NaCl', 'rocksalt', a=5.64)

# Save to CIF format
write('nacl.cif', nacl)

# Read back
nacl_read = read('nacl.cif')

# Get spacegroup information
sg = get_spacegroup(nacl_read)

# Print spacegroup info and number of atoms
print(f"Spacegroup: {sg}")
print(f"Number of atoms: {len(nacl_read)}")
