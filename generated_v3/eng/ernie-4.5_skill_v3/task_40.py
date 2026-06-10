from ase.build import bulk
from ase.io import read, write
from ase.spacegroup import get_spacegroup

# Create NaCl crystal (rock salt structure, spacegroup Fm-3m)
atoms = bulk('NaCl', 'rocksalt', a=5.64, orthorhombic=False)

# Write to CIF file
write('nacl.cif', atoms)

# Read back from CIF file
atoms_read = read('nacl.cif')

# Get and print spacegroup information
sg = get_spacegroup(atoms_read)
print(f"Spacegroup: {sg.symbol} ({sg.no})")
print(f"International table symbol: {sg.international}")
print(f"Number of atoms: {len(atoms_read)}")
