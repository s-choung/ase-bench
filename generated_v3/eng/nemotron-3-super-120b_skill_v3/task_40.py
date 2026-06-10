from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import get_spacegroup

# Create NaCl rock-salt crystal
atoms = bulk('NaCl', 'rocksalt', a=5.64)

# Write to CIF
write('NaCl.cif', atoms)

# Read back from CIF
atoms_read = read('NaCl.cif')

# Get spacegroup information
sg = get_spacegroup(atoms_read)
print(f"Spacegroup number: {sg.no}")
print(f"Spacegroup symbol: {sg.symbol}")

# Print number of atoms
print(f"Number of atoms: {len(atoms_read)}")
