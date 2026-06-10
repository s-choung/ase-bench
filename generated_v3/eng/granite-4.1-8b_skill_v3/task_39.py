from ase import Atoms
from ase.build import bulk

# Create Au FCC bulk
atoms = bulk('Au', 'fcc', a=4.0)

# Save to XYZ format
atoms.write('Au_fcc.xyz')

# Read back from XYZ file
atoms_read = atoms.copy()
atoms_read.read('Au_fcc.xyz')

# Print atom types and positions
print("Atom types:", atoms_read.get_chemical_symbols())
print("Positions (in Angstroms):")
print(atoms_read.get_positions())
