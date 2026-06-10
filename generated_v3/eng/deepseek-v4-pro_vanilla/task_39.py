from ase.build import bulk
from ase.io import write, read

# Create Au FCC bulk structure
atoms = bulk('Au', 'fcc', a=4.08)

# Save to XYZ format
write('au_fcc.xyz', atoms)

# Read the structure back
atoms_read = read('au_fcc.xyz')

# Print atom types and positions
for sym, pos in zip(atoms_read.get_chemical_symbols(), atoms_read.positions):
    print(f"Atom type: {sym}, Position: {pos}")
