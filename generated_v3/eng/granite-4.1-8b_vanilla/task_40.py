from ase import Atoms
from ase.io import write, read
from ase.crystal import Crystal

# Create NaCl crystal structure
NaCl = Crystal('NaCl', size=(1, 1, 1), a=5.64, spgnum=225)  # Rocksalt structure, spacegroup 225

# Write the structure to a CIF file
write('NaCl.cif', NaCl)

# Read the structure back from the CIF file
structure = read('NaCl.cif')

# Print spacegroup information and number of atoms
print(f"Spacegroup: {structure.get_spacegroup()}")
print(f"Number of atoms: {len(structure)}")
