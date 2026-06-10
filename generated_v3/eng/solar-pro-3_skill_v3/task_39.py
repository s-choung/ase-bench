from ase.build import bulk
from ase.io import write, read

# Build Au FCC bulk with side length 5 Å
atoms = bulk('Au', 'fcc', cubic=True, a=4.08) * 5

# Write to XYZ file (overwrites if exists)
write('Au_fcc.xyz', atoms)

# Read back from XYZ file
atoms_back = read('Au_fcc.xyz')

# Print atom types and positions in Ångströms
for i, a in enumerate(atoms_back):
    print(f"Atom {i}: type='{a.symbol}', pos={a.position:.3f}")
