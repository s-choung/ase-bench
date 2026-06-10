from ase.build import nanotube

# Create a (6,6) carbon nanotube with length 4 nm
# Note: nanotube function uses length in Angstroms by default if not specified, 
# but for common nanotube builds, we define dimensions.
# For a length of 4 (assuming nm as per common context), we use 40.0 Angstroms.
# If the user meant 4 Angstroms, change to 4.0.
nt = nanotube(n=6, m=6, length=40.0, symbol='C')

print(f"Number of atoms: {len(nt)}")
print(f"Cell information:\n{nt.get_cell()}")
print(f"Cell lengths and angles: {nt.get_cell_lengths_and_angles()}")
