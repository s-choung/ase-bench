from ase.build import bulk
from ase.io import read, write
from ase.spacegroup import get_spacegroup

# Build NaCl conventional cubic cell (rocksalt structure)
nacl = bulk('NaCl', 'rocksalt', a=5.64, cubic=True)
# Write to CIF
write('NaCl.cif', nacl, format='cif')
# Read back from CIF
nacl_read = read('NaCl.cif', format='cif')
# Get spacegroup and atom count
spacegroup = get_spacegroup(nacl_read)
atom_count = len(nacl_read)
# Print results
print(f"Spacegroup: {spacegroup.symbol} (number {spacegroup.no})")
print(f"Number of atoms: {atom_count}")
