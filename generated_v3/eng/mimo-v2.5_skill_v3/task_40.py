from ase.spacegroup import crystal
from ase.io import write, read

# Create NaCl rocksalt structure (spacegroup 225, Fm-3m)
nacl = crystal(
    ['Na', 'Cl'],
    basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
    spacegroup=225,
    cellpar=[5.64, 5.64, 5.64, 90, 90, 90]
)

print("=== Original Structure ===")
print(f"Space group: {nacl.get_spacegroup()}")
print(f"Number of atoms: {len(nacl)}")

# Save to CIF
write('NaCl.cif', nacl)

# Read back from CIF
nacl_read = read('NaCl.cif')

print("\n=== Read Back from CIF ===")
print(f"Space group: {nacl_read.get_spacegroup()}")
print(f"Number of atoms: {len(nacl_read)}")
