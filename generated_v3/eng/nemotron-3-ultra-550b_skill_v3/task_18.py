from ase.build import molecule
from ase.geometry import get_distances

atoms = molecule('CH4')

print("Atomic coordinates:")
for atom in atoms:
    print(f"  {atom.symbol}: {atom.position}")

print("\nBond lengths (Å):")
positions = atoms.get_positions()
cell = atoms.get_cell()
pbc = atoms.get_pbc()
for i in range(len(atoms)):
    for j in range(i + 1, len(atoms)):
        d, _ = get_distances(positions[i], positions[j], cell, pbc)
        print(f"  {atoms[i].symbol}{i}-{atoms[j].symbol}{j}: {d:.4f}")

print(f"\nChemical formula: {atoms.get_chemical_formula()}")
