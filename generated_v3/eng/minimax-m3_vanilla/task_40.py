from ase.build import bulk
from ase.io import read, write
from ase.spacegroup import get_spacegroup

# Create NaCl crystal
atoms = bulk('NaCl', 'rocksalt', a=5.64)

# Save as CIF
write('nacl.cif', atoms)

# Read it back
atoms_read = read('nacl.cif')

# Get spacegroup info
sg = get_spacegroup(atoms_read)
print(f"Spacegroup: {sg.symbol} ({sg.no})")
print(f"International: {sg.international}")
print(f"Number of atoms: {len(atoms_read)}")
