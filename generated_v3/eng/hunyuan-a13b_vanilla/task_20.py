from ase import Atoms, Cell
from ase.calculators import EMT

# Create (6,6) carbon nanotube
cnt_length = 4  # Repeat velocity vector in edges [a1, a2, a3]
cnt_n = 6  # Number of atoms in each circular direction
a = 2.7  # Lattice constant (Angstrom)
carbon = Atoms('C', positions=[(0, 0, 0),
                           (a, 0, 0),
                           (a * cnt_n, 0, 0),
                           (0, a, 0),
                           (0, a * 2, 0),
                           (0, a * 3, 0),
                           (0, a * 4, 0),
                           (0, a * 5, 0),
                           (0, a * 6, 0),
                           (0, a * 7, 0),
                           (0, a * 8, 0),
                           (0, a * 9, 0)],
               cell=(a * cnt_n, a, a),
               pbc=[True, False, False])
cnt_length.push(0, 0, -cnt_length * a)  # Translate third direction

# Print cell info
print("Cell vectors:")
for vec in cnt_length.cell:
    print(vec)

# Print number of atoms
print(f"Number of atoms: {len(cnt_length)}")
