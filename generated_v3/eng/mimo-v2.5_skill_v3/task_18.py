from ase.collections import g2
from ase.geometry import distance

atoms = g2['CH4']

print(f"Chemical formula: {atoms.get_chemical_formula()}")
print(f"\nAtomic coordinates:\n{atoms.get_positions()}")

print("\nBond lengths (Å):")
for i in range(len(atoms)):
    for j in range(i + 1, len(atoms)):
        d = distance(atoms, i, j)
        if d < 1.6:
            print(f"  {atoms.symbols[i]}({i})-{atoms.symbols[j]}({j}): {d:.4f}")
