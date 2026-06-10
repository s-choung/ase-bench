from ase.build import molecule
from ase.geometry import get_distances
import numpy as np

ch4 = molecule('CH4')

print("=== Chemical Formula ===")
print(ch4.get_chemical_formula())

print("\n=== Atomic Positions ===")
print(f"{'Atom':<6} {'x':>10} {'y':>10} {'z':>10}")
print("-" * 38)
for atom in ch4:
    x, y, z = atom.position
    print(f"{atom.symbol:<6} {x:>10.4f} {y:>10.4f} {z:>10.4f}")

print("\n=== Bond Lengths ===")
positions = ch4.get_positions()
symbols = ch4.get_chemical_symbols()
c_idx = [i for i, s in enumerate(symbols) if s == 'C'][0]
h_indices = [i for i, s in enumerate(symbols) if s == 'H']

for h_idx in h_indices:
    diff = positions[h_idx] - positions[c_idx]
    dist = np.linalg.norm(diff)
    print(f"C-H (atom {c_idx}-{h_idx}): {dist:.4f} Å")
