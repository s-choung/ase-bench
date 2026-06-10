from ase.collections import g2
from ase.geometry import get_distances

atoms = g2['CH4']

print("Chemical formula:", atoms.get_chemical_formula())
print("Atomic coordinates (Å):")
for i, (sym, pos) in enumerate(zip(atoms.get_chemical_symbols(), atoms.get_positions()), 1):
    print(f"{i:2d} {sym:2s} {pos[0]: .6f} {pos[1]: .6f} {pos[2]: .6f}")

print("Bond lengths (Å):")
for i in range(1, len(atoms)):
    d = atoms.get_distance(0, i)
    print(f"C-{atoms[i].symbol}{i}: {d:.6f}")
