from ase.build import molecule
from ase.geometry import get_distances

ch4 = molecule('CH4')
print("Atomic coordinates (Å):")
print(ch4.positions)
print("\nBond lengths (Å):")
distances = get_distances(ch4.positions)[1]
print(distances[distances > 0].min())  # minimum non-zero distance
print("\nChemical formula:")
print(ch4.get_chemical_formula())
