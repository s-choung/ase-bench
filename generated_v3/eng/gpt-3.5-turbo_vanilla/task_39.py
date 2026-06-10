import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.io import write, read

# Create FCC bulk Au
a = 4.08
atoms = bulk('Au', 'fcc', a=a)

# Write atoms to XYZ file
write('Au_FCC.xyz', atoms)

# Read atoms back from XYZ file
atoms_read = read('Au_FCC.xyz')

# Print atom types and positions
print(atoms_read.get_chemical_symbols())
print(atoms_read.get_positions())
