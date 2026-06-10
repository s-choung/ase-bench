from ase.build import bulk
from ase.io import write, read

# Create FCC gold bulk structure (conventional cell)
atoms = bulk('Au', 'fcc', a=4.08, cubic=True)
write('au_fcc.xyz', atoms)

# Read structure from XYZ file
atoms_loaded = read('au_fcc.xyz')

# Print atom types and positions
print("Element\t X\t\t Y\t\t Z")
for atom in atoms_loaded:
    symbol = atom.symbol
    pos = atom.position
    print(f"{symbol}\t {pos[0]:.6f}\t {pos[1]:.6f}\t {pos[2]:.6f}")
