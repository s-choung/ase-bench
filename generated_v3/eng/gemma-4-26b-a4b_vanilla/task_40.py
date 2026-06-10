from ase.build import bulk
from ase.io import write, read

# Create NaCl structure (Rock salt, Fm-3m)
atoms = bulk('NaCl', 'rocksalt', a=5.64)

# Save to CIF
write('nacl.cif', atoms)

# Read back
atoms_read = read('nacl.cif')

# Print info
print(f"Spacegroup: {atoms_read.get_spacegroup()}")
print(f"Number of atoms: {len(atoms_read)}")
