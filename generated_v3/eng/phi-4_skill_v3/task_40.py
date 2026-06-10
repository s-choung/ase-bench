from ase import Atoms
from ase.build import bulk
from ase.io import write, read
from ase.geometry import get_spacegroup

# Create NaCl crystal structure
nacl = bulk('NaCl', 'rocksalt', a=5.64, cubic=True)

# Write the structure to a CIF file
write(nacl, 'NaCl.cif', format='cif')

# Read the structure back from the CIF file
nacl_cif = read('NaCl.cif', format='cif')

# Print spacegroup information and number of atoms
spacegroup = get_spacegroup(nacl_cif)
print(f'Spacegroup: {spacegroup}')
print(f'Number of atoms: {len(nacl_cif)}')
