from ase.collections import g2
from ase.geometry import get_distances

ch4 = g2['CH4']

print("Chemical formula:", ch4.get_chemical_formula())
print("Atomic coordinates (Å):")
for i, (sym, pos) in enumerate(zip(ch4.get_chemical_symbols(), ch4.get_positions())):
    print(f"{i:2d} {sym:2s} {pos[0]: .6f} {pos[1]: .6f} {pos[2]: .6f}")

print("\nBond lengths (Å):")
for i in range(len(ch4)):
    for j in range(i + 1, len(ch4)):
        d = ch4.get_distance(i, j)
        print(f"{i}-{j}: {d:.6f}")
