from ase import Atoms
from ase.spacegroup import crystal
from ase.io import write, read
import numpy as np

# Create NaCl crystal structure (rock salt, space group Fm-3m)
a = 5.64  # lattice parameter in Angstrom
atoms = crystal('NaCl', basis=['Na', 'Cl'], spacegroup=225, 
                cellpar=[a, a, a, 90, 90, 90])

# Save to CIF file
write('nacl.cif', atoms)

# Read back from CIF
atoms_read = read('nacl.cif')

# Print spacegroup information and number of atoms
spacegroup = atoms_read.get_spacegroup()
print(f"Spacegroup: {spacegroup}")
print(f"Number of atoms: {len(atoms_read)}")
