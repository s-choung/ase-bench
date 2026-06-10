from ase.build import bulk
from ase.io import write, read
import ase.spacegroup

# Create NaCl crystal structure (rock salt)
atoms = bulk('NaCl', crystalstructure='rocksalt', a=5.64, cubic=True)

# Save to CIF
write('nacl.cif', atoms)

# Read back from CIF
atoms2 = read('nacl.cif')

# Print results
print('Spacegroup:', ase.spacegroup.get_spacegroup(atoms2))
print('Number of atoms:', len(atoms2))
