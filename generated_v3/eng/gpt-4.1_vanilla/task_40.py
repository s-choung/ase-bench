from ase.build import bulk
from ase.io import write, read

# Create and save NaCl structure
nacl = bulk('NaCl', 'rocksalt', a=5.64)
write('nacl.cif', nacl)

# Read back the CIF file
nacl_read = read('nacl.cif')

# Print spacegroup info and number of atoms
sg = nacl_read.info.get('spacegroup', {})
print(f"Spacegroup: {sg.get('InternationalNumber', 'Unknown')} ({sg.get('InternationalShortSymbol', 'Unknown')})")
print(f"Number of atoms: {len(nacl_read)}")
