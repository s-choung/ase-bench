from ase.spacegroup import crystal
from ase.io import write, read

# Create NaCl crystal
a = 5.64
nacl = crystal('NaCl', [(0, 0, 0), (0.5, 0.5, 0.5)],
              spacegroup=225, cellpar=[a, a, a, 90, 90, 90])

# Write to CIF file
write('nacl.cif', nacl)

# Read CIF file
nacl_read = read('nacl.cif')

# Get spacegroup information
from ase.utils.spacegroup import get_spacegroup
sg = get_spacegroup(nacl_read)

# Print results
print(f'Spacegroup: {sg["number"]} ({sg["symbol"]})')
print(f'Number of atoms: {len(nacl_read)}')
