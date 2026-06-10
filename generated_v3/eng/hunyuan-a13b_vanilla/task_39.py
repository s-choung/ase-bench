from ase import Atom, Atoms
from ase.io import write, read

# Create Au FCC bulk
fcc_cells = [
    [2.66, 0.0, 0.0],
    [0.0, 2.66, 0.0],
    [0.0, 0.0, 2.66]
]
fcc_atoms = [
    Atom('Au', (0.0, 0.0, 0.0)),
    Atom('Au', (0.5, 0.5, 0.0)),
    Atom('Au', (0.5, 0.0, 0.5)),
    Atom('Au', (0.0, 0.5, 0.5))
]
bulk = Atoms(fcc_atoms, fcc_cells)

# Save to XYZ
write('au_fcc.xyz', bulk)

# Read back
bulk_read = read('au_fcc.xyz')

# Print atom types and positions
for atom in bulk_read:
    print(f"Atom: {atom.symbol}, Position: {atom.position}")
