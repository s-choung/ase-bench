from ase.build import bulk
from ase.io import write, read

# Create FCC Au bulk
atoms = bulk('Au', 'fcc', a=4.08)

# Save to XYZ and read back
xyz_file = 'au_fcc.xyz'
write(xyz_file, atoms, format='xyz')
atoms_back = read(xyz_file)

# Print atom types and positions
for i, atom in enumerate(atoms_back):
    print(f"{i+1}: {atom.symbol}  {atom.position}")
