from ase import Atoms
from ase.build import bulk
from ase.io import write, read

# Create FCC bulk of gold
atoms = bulk('Au', 'fcc', a=4.08)

# Save to an XYZ file
write('au_bulk.xyz', atoms)

# Read back the atoms
atoms_read = read('au_bulk.xyz')

# Print atom types and positions
for atom in atoms_read:
    print(atom.symbol, atom.position)
