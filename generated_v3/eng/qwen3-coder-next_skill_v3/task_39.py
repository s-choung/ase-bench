from ase import Atoms
from ase.build import bulk
from ase.io import write, read

# Create Au FCC bulk
atoms = bulk('Au', 'fcc', a=4.08)

# Save to XYZ format
write('Au_fcc.xyz', atoms, format='xyz')

# Read back
read_atoms = read('Au_fcc.xyz', format='xyz')

# Print atom types and positions
symbols = read_atoms.get_chemical_symbols()
positions = read_atoms.get_positions()

print("Atom types:", symbols)
print("Positions (Å):")
for i, (symbol, pos) in enumerate(zip(symbols, positions)):
    print(f"  {i}: {symbol} at ({pos[0]:.4f}, {pos[1]:.4f}, {pos[2]:.4f})")
