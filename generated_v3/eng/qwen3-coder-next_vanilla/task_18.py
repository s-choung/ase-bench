from ase import Atoms
from ase.data import g2

# Retrieve CH4 molecule from G2 database
atoms = g2[0]['CH4']

# Print chemical formula
print("Formula:", atoms.get_chemical_formula())

# Print atomic coordinates (in Angstrom)
print("\nAtomic coordinates (Angstrom):")
for i, (symbol, pos) in enumerate(zip(atoms.get_chemical_symbols(), atoms.get_positions())):
    print(f"{symbol} {i}: ({pos[0]:.4f}, {pos[1]:.4f}, {pos[2]:.4f})")

# Print C-H bond lengths
positions = atoms.get_positions()
c_pos = positions[0]  # Carbon is first atom in CH4
h_positions = positions[1:]

print("\nC-H bond lengths (Angstrom):")
for i, h_pos in enumerate(h_positions):
    distance = ((h_pos - c_pos)**2).sum()**0.5
    print(f"C-H{i+1}: {distance:.4f}")
