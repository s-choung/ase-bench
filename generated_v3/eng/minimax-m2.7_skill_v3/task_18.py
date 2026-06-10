from ase.collections import g2
import numpy as np

ch4 = g2['CH4']

print("Chemical formula:", ch4.get_chemical_formula())
print("\nAtomic coordinates (Å):")
print(ch4.get_positions())

symbols = ch4.get_chemical_symbols()
c_idx = symbols.index('C')
h_indices = [i for i, s in enumerate(symbols) if s == 'H']

print("\nBond lengths (C-H):")
for h_idx in h_indices:
    dist = np.linalg.norm(ch4.positions[c_idx] - ch4.positions[h_idx])
    print(f"  {dist:.4f} Å")
