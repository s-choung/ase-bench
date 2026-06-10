from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import get_spacegroup

# Create NaCl rocksalt structure
na_cl = bulk('NaCl', crystalstructure='rocksalt', a=5.64)

# Write to CIF file
write('nacl.cif', na_cl)

# Read back the CIF file
na_cl_read = read('nacl.cif')

# Get spacegroup information
sg = get_spacegroup(na_cl_read)

# Print spacegroup and number of atoms
print(f"Spacegroup: {sg.symbol} ({sg.no})")
print(f"Number of atoms: {len(na_cl_read)}")
