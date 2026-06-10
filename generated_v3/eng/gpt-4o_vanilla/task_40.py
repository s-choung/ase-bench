from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import get_spacegroup

# Create NaCl bulk structure
nacl = bulk('NaCl', 'rocksalt', a=5.64)

# Save to CIF format
write('nacl.cif', nacl)

# Read the structure back
nacl_read = read('nacl.cif')

# Get spacegroup and number of atoms
spacegroup = get_spacegroup(nacl_read)
num_atoms = len(nacl_read)

print(f"Spacegroup: {spacegroup}")
print(f"Number of atoms: {num_atoms}")
