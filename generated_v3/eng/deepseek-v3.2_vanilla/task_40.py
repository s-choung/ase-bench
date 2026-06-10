from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import get_spacegroup

# Create NaCl crystal structure
atoms = bulk('NaCl', crystalstructure='rocksalt', a=5.64)

# Write to CIF file
write('nacl.cif', atoms)

# Read back from CIF file
atoms_loaded = read('nacl.cif')

# Print spacegroup information and number of atoms
sg = get_spacegroup(atoms_loaded)
print(f"Spacegroup: {sg.symbol} (number {sg.no})")
print(f"Number of atoms: {len(atoms_loaded)}")
