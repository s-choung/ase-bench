from ase.db import connect

# Connect to ASE's built-in G2 database and retrieve CH4
db = connect('g2')
ch4_row = db.get(formula='CH4')
atoms = ch4_row.toatoms()

# Print chemical formula
print(f"Chemical Formula: {atoms.get_chemical_formula()}\n")

# Print atomic coordinates
print("Atomic Coordinates (Å):")
for atom in atoms:
    print(f"{atom.symbol:2} {atom.position[0]:.4f} {atom.position[1]:.4f} {atom.position[2]:.4f}")

# Calculate and print C-H bond lengths
dist_matrix = atoms.get_all_distances()
c_index = next(i for i, a in enumerate(atoms) if a.symbol == 'C')
h_indices = [i for i, a in enumerate(atoms) if a.symbol == 'H']
print("\nC-H Bond Lengths (Å):")
for h_idx in h_indices:
    print(f"{dist_matrix[c_index, h_idx]:.4f}")
