from ase.spacegroup import crystal
from ase.io import write, read
from ase.spacegroup import get_spacegroup

# Create NaCl crystal (spacegroup 225, Fm-3m)
a = 5.64  # lattice constant in Angstrom
nacl = crystal(['Na', 'Cl'], [(0, 0, 0), (0.5, 0.5, 0.5)],
               spacegroup=225, cellpar=[a, a, a, 90, 90, 90])

# Save to CIF
write('nacl.cif', nacl, format='cif')

# Read back
nacl_read = read('nacl.cif', format='cif')

# Spacegroup info
spg = get_spacegroup(nacl_read)
print(f"Spacegroup: {spg}")
print(f"Number of atoms: {len(nacl_read)}")
