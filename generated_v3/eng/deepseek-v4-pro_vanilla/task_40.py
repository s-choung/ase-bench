from ase.spacegroup import crystal
from ase.io import write, read
from ase.spacegroup import get_spacegroup

# Create NaCl crystal
a = 5.64
nacl = crystal(['Na', 'Cl'],
               basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
               spacegroup=225,
               cellpar=[a, a, a, 90, 90, 90])

# Save to CIF
write('nacl.cif', nacl)

# Read back
nacl_read = read('nacl.cif')

# Print info
spacegroup = get_spacegroup(nacl_read)
print(f"Spacegroup: {spacegroup}")
print(f"Number of atoms: {len(nacl_read)}")
