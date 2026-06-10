from ase import Atoms
from ase.build import bulk
from ase.io import write, read

# Create Au FCC bulk
atoms = bulk('Au', 'fcc', a=4.0)

# Save to XYZ format file
write('Au_fcc.xyz', atoms, format='xyz')

# Read back the XYZ file
read_atoms = read('Au_fcc.xyz', format='xyz')

# Print atom types and positions
print('Atom types:', read_atoms.get_chemical_symbols())
print('Atom positions:')
for idx, pos in enumerate(read_atoms.get_positions()):
    print(f'Atom {idx+1}: {pos}')
