from ase.build import molecule
from ase.io import read
import numpy as np

# CH4 분자 생성
ch4 = molecule('CH4')

# Chemical formula
print(f"Chemical Formula: {ch4.get_chemical_formula()}")
print(f"\nAtomic Coordinates:")
print(f"{'Atom':<6} {'X (Å)':<12} {'Y (Å)':<12} {'Z (Å)':<12}")
print("-" * 42)
for i, (symbol, pos) in enumerate(zip(ch4.get_chemical_symbols(), ch4.get_positions())):
    print(f"{symbol:<6} {pos[0]:<12.6f} {pos[1]:<12.6f} {pos[2]:<12.6f}")

# Bond lengths (C-H)
positions = ch4.get_positions()
c_pos = positions[0]
h_positions = positions[1:]

print(f"\nBond Lengths (C-H):")
for i, h_pos in enumerate(h_positions):
    bond_length = np.linalg.norm(h_pos - c_pos)
    print(f"C-H{i+1}: {bond_length:.6f} Å")
