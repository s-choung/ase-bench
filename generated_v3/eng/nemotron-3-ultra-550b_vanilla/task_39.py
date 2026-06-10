from ase.build import bulk
from ase.io import write, read

# Create Au FCC bulk
atoms = bulk('Au', 'fcc', a=4.08, cubic=True)

# Save to XYZ
write('au_bulk.xyz', atoms)

# Read back
atoms_read = read('au_bulk.xyz')

# Print atom types and positions
for atom in atoms_read:
    print(f"{atom.symbol} {atom.position[0]:.4f} {atom.position[1]:.4f} {atom.position[2]:.4f}")
