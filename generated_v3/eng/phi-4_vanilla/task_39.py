from ase import Atoms
from ase.io import read, write

# Create an FCC Au bulk using EMT calculator
Au_bulk = Atoms('Au', positions=[(0, 0, 0)], cell=[4.078, 4.078, 4.078], pbc=[True, True, True])
Au_bulk.set_calculator('emt')

# Save to an XYZ file
write('Au_bulk.xyz', Au_bulk)

# Read the XYZ file
read_atoms = read('Au_bulk.xyz')
print(read_atoms.get_chemical_symbols())  # Print atom types
print(read_atoms.get_positions())         # Print positions

# Clean up the XYZ file (remove after verification)
import os
os.remove('Au_bulk.xyz')
