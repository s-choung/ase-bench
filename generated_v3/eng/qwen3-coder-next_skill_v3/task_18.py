from ase.collections import g2
from ase import units

# Retrieve CH4 from G2 database
atoms = g2['CH4']

# Print chemical formula
print(f"Chemical formula: {atoms.get_chemical_formula()}")

# Print atomic coordinates (in Angstrom)
print("Atomic coordinates (Angstrom):")
for i, (symbol, pos) in enumerate(zip(atoms.get_chemical_symbols(), atoms.get_positions())):
    print(f"  {i:2d} {symbol}  {pos[0]:8.4f}  {pos[1]:8.4f}  {pos[2]:8.4f}")

# Calculate and print C-H bond lengths
C_idx = [i for i, s in enumerate(atoms.get_chemical_symbols()) if s == 'C'][0]
H_indices = [i for i, s in enumerate(atoms.get_chemical_symbols()) if s == 'H']
print("\nC-H bond lengths (Angstrom):")
for H_idx in H_indices:
    dist = atoms.get_distance(C_idx, H_idx)
    print(f"  C-H({H_idx}): {dist:.4f}")
