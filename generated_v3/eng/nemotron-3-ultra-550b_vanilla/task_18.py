from ase.data.g2 import data
from ase.geometry import get_distances

atoms = data['CH4']['atoms']

print("Atomic coordinates:")
for atom in atoms:
    print(f"  {atom.symbol}: {atom.position}")

print("\nBond lengths (Å):")
positions = atoms.get_positions()
cell = atoms.get_cell()
pbc = atoms.get_pbc()
distances, _ = get_distances(positions, positions, cell=cell, pbc=pbc)
for i in range(len(atoms)):
    for j in range(i + 1, len(atoms)):
        d = distances[i, j]
        if d < 1.5:
            print(f"  {atoms[i].symbol}{i}-{atoms[j].symbol}{j}: {d:.4f}")

print(f"\nChemical formula: {atoms.get_chemical_formula()}")
