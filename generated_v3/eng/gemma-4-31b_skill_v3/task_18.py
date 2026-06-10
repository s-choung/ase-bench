from ase.build import molecule
from ase.geometry import get_distances

# Retrieve CH4 from G2 database
atoms = molecule('CH4')

# Print atomic coordinates
print("Atomic Coordinates:\n", atoms.get_positions())

# Calculate and print bond lengths (C is index 0, H are indices 1-4)
# Since it's CH4, all bonds are between index 0 and the rest
bond_lengths = [get_distances(atoms[0], atoms[i]) for i in range(1, 5)]
print("Bond Lengths (C-H):", bond_lengths)

# Print chemical formula
print("Chemical Formula:", atoms.get_chemical_formula())
