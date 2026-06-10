from ase.build import bulk
from ase.io import read, write

# Create NaCl crystal structure
atoms = bulk('NaCl', 'rocksalt', a=5.64, cubic=True)

# Save to CIF and read back
write('NaCl.cif', atoms)
atoms = read('NaCl.cif')

# Print spacegroup and number of atoms
sg = atoms.get_spacegroup()
print(f"Spacegroup: {sg}")
print(f"Number of atoms: {len(atoms)}")
