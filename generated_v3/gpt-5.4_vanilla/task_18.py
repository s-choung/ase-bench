from ase.collections import g2
from ase.geometry import get_distances

atoms = g2['CH4']

print("Chemical formula:", atoms.get_chemical_formula())
print("Atomic coordinates:")
for i, atom in enumerate(atoms):
    x, y, z = atom.position
    print(f"{i:2d} {atom.symbol:2s} {x:12.6f} {y:12.6f} {z:12.6f}")

print("Bond lengths:")
for i in range(len(atoms)):
    for j in range(i + 1, len(atoms)):
        d = atoms.get_distance(i, j)
        print(f"{i}-{j} ({atoms[i].symbol}-{atoms[j].symbol}): {d:.6f} Å")
