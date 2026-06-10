from ase.build import molecule
from ase.geometry import get_distances

atoms = molecule('CH4')
print("Chemical formula:", atoms.get_chemical_formula())
print("Atomic coordinates (Å):")
for atom in atoms:
    print(f"{atom.symbol:2s} {atom.position}")

distances = get_distances(atoms.positions)[1]
print("\nBond lengths (Å):")
for i in range(1, 5):
    print(f"C-H{i}: {distances[0, i]:.3f}")
