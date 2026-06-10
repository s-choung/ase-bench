from ase import Atom, Atoms
from ase.io import write, read
from ase.spacegroup import SpaceGroup

# Build NaCl structure
NaCl = Atoms('NaCl', positions=[(0, 0, 0), (0.5, 0.5, 0.5)],
               cell=[10.2, 10.2, 10.2])

# Save to CIF
write('NaCl.cif', NaCl)

# Read back
NaCl_read = read('NaCl.cif')

# Print spacegroup and number of atoms
sg = SpaceGroup.from_cell(NaCl_read.cell, NaCl_read.get_symmetry_matrix())
print(f"SpaceGroup: {sgponent}")
print(f"Number of atoms: {len(NaCl_read)}")
