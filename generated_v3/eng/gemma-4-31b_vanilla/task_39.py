from ase.build import bulk
from ase.io import write, read

# Create Au FCC bulk
atoms = bulk('Au', 'fcc', a=4.08)

# Save to XYZ
write('gold.xyz', atoms)

# Read back from XYZ
loaded_atoms = read('gold.xyz')

# Print atom types and positions
for atom in loaded_atoms:
    print(f"Symbol: {atom.symbol}, Position: {atom.position}")
