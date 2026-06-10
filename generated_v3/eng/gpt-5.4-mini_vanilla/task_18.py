from ase.collections import g2
from ase.geometry import get_distances

atoms = g2['CH4']

print("Chemical formula:", atoms.get_chemical_formula())
print("Atomic coordinates (Å):")
for sym, pos in zip(atoms.get_chemical_symbols(), atoms.get_positions()):
    print(f"{sym:2s}  {pos[0]: .6f}  {pos[1]: .6f}  {pos[2]: .6f}")

print("\nBond lengths (Å):")
for i in range(1, len(atoms)):
    d = atoms.get_distance(0, i)
    print(f"C-{atoms[i].symbol}{i}: {d:.6f}")
