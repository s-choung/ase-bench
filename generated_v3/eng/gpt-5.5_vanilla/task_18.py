from ase.collections import g2
from ase.data import covalent_radii

atoms = g2["CH4"]

print("Atomic coordinates (Å):")
for atom in atoms:
    x, y, z = atom.position
    print(f"{atom.symbol:2s} {x:10.6f} {y:10.6f} {z:10.6f}")

print("\nBond lengths (Å):")
for i in range(len(atoms)):
    for j in range(i + 1, len(atoms)):
        cutoff = 1.2 * (covalent_radii[atoms[i].number] + covalent_radii[atoms[j].number])
        d = atoms.get_distance(i, j)
        if d <= cutoff:
            print(f"{atoms[i].symbol}{i}-{atoms[j].symbol}{j}: {d:.6f}")

print("\nChemical formula:")
print(atoms.get_chemical_formula())
