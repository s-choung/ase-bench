from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import crystal

# Create NaCl structure
atoms = bulk('NaCl', 'rocksalt', a=5.64)

# Save as CIF
write('nacl.cif', atoms, format='cif')

# Read back
atoms_read = read('nacl.cif')

# Print spacegroup info (by checking symmetry) and atom count
# Note: atoms.get_cell_lengths_and_angles() returns [a, b, c, alpha, beta, gamma]
print(f"Atoms: {len(atoms_read)}")
print(f"Cell parameters: {atoms_read.get_cell_lengths_and_angles()}")
