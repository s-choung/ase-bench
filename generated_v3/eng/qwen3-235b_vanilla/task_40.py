from ase import Atoms
from ase.spacegroup import crystal
from ase.io import write, read

# Create NaCl crystal structure
nacl = crystal(['Na', 'Cl'], [(0, 0, 0), (0.5, 0.5, 0.5)],
               spacegroup=225, cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

# Write to CIF file
write('nacl.cif', nacl)

# Read back the structure
nacl_read = read('nacl.cif')

# Print spacegroup (ASE does not store spacegroup in CIF by default, so infer it)
from ase.spacegroup import get_spacegroup
sg = get_spacegroup(nacl_read)
print(f"Spacegroup: {sg.symbol}, Number: {sg.no}")
print(f"Number of atoms: {len(nacl_read)}")
