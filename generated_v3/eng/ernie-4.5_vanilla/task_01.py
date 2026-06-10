from ase.build import bulk
from ase.build import make_supercell

# Create a Cu FCC crystal
cu_bulk = bulk('Cu', 'fcc', a=3.61, cubic=True)

# Generate a 2x2x2 supercell
supercell_matrix = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]
cu_supercell = make_supercell(cu_bulk, supercell_matrix)

# Print cell information
print("Cell lattice vectors (in Angstrom):")
for vector in cu_supercell.cell:
    print(vector)

# Print number of atoms
print(f"Number of atoms: {len(cu_supercell)}")
