from ase.build import bulk
from ase.io import read, write
from ase.spacegroup import get_spacegroup

# Generate NaCl rocksalt unit cell
nacl = bulk("NaCl", crystalstructure="rocksalt", a=5.64)

# Save structure to CIF format
write("nacl.cif", nacl)

# Read CIF file back into an atoms object
reloaded_nacl = read("nacl.cif")

# Extract and print required information
sg = get_spacegroup(reloaded_nacl)
print(f"Spacegroup: {sg.symbol} (International Tables number: {sg.no})")
print(f"Total number of atoms in unit cell: {len(reloaded_nacl)}")
