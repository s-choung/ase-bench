from ase.build import rocksalt
from ase.io import read, write
from ase.spacegroup import get_spacegroup

# Create NaCl crystal (rocksalt) with lattice constant ~5.64 Å
atoms = rocksalt(['Na', 'Cl'], latticeconstant=5.64)

# Write to CIF
write('NaCl.cif', atoms)

# Read back
atoms_read = read('NaCl.cif')

# Spacegroup information
sg = get_spacegroup(atoms_read)
print(f"Spacegroup: {sg.symbol} (No. {sg.no})")

# Number of atoms
print(f"Number of atoms: {len(atoms_read)}")
