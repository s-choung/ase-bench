from ase import Atoms
from ase.build import molecule
from ase.geometry import get_distances

ch4 = molecule('CH4')

coords = ch4.get_positions()
formula = ch4.get_chemical_formula()

distances, _ = get_distances(ch4)

print("Coordinates:")
print(coords)
print("\nBond Lengths (Å):")
print(distances[0, 1:])
print("\nChemical Formula:")
print(formula)
