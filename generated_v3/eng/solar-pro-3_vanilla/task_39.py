from ase import Atoms, io

# Define FCC bulk Au
a = 4.078  # angstrom
Au = Atoms('Au4',
           cell=(a, a, a),
           pbc=True,
           positions=[[0,0,0],
                     [0,1/2,1/2],
                     [1/2,0,1/2],
                     [1/2,1/2,0]])

# Write to XYZ file
io.xyz.write(Au, 'Au_fcc_bulk.xyz')

# Read back from XYZ file
Au2 = io.xyz.read('Au_fcc_bulk.xyz')

# Print atom types and positions
for idx, atom in enumerate(Au2):
    print(f"Atom {idx}: type={atom.symbol}, position={atom.position}")
