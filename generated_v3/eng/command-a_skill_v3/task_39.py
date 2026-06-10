from ase import Atoms
from ase.build import bulk
from ase.io import write, read

# Create Au FCC bulk
atoms = bulk('Au', 'fcc', a=4.078, cubic=True)

# Write to XYZ file
write('Au_fcc.xyz', atoms)

# Read from XYZ file
atoms_read = read('Au_fcc.xyz')

# Print atom types and positions
for atom in atoms_read:
    print(f"{atom.symbol}: {atom.position}")
