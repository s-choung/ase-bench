from ase.collections import g2
from ase import Atoms

ch4 = g2['CH4']
symbols = ch4.get_chemical_symbols()
positions = ch4.get_positions()

print("Atomic coordinates:")
for symbol, pos in zip(symbols, positions):
    print(f"{symbol:2s} {pos[0]:10.5f} {pos[1]:10.5f} {pos[2]:10.5f} Å")

c_idx = [i for i, sym in enumerate(symbols) if sym == 'C'][0]
h_indices = [i for i, sym in enumerate(symbols) if sym == 'H']

print("\nBond lengths:")
for j, h_idx in enumerate(h_indices, 1):
    bond_length = ch4.get_distance(c_idx, h_idx)
    print(f"C-H{j}: {bond_length:.5f} Å")

print(f"\nChemical formula: {ch4.get_chemical_formula()}")
