from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.io import write, read

# Create Au FCC bulk
atoms = FaceCenteredCubic('Au', size=(1, 1, 1), pbc=True)

# Save to XYZ
write('au_fcc.xyz', atoms)

# Read back
atoms_read = read('au_fcc.xyz')[0]

# Print atom types and positions
print("Atom types:", atoms_read.get_chemical_symbols())
print("Positions:\n", atoms_read.get_positions())
