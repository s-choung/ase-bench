from ase.build import bulk
from ase.io import write, read

# Create a gold FCC bulk structure
gold_bulk = bulk('Au', 'fcc', a=4.08, cubic=True)

# Write the structure to an XYZ file
write('gold_bulk.xyz', gold_bulk)

# Read the structure back from the XYZ file
loaded_structure = read('gold_bulk.xyz')

# Print the atom types and positions
print("Atom types and positions:")
for atom in loaded_structure:
    print(f"Atom {atom.symbol} at position {atom.position}")
