from ase.build import molecule
from ase.io import write
from ase.visualize import view
import numpy as np

# Retrieve the CH4 molecule
ch4 = molecule('CH4')

# Print the atomic coordinates
print("Atomic Coordinates:")
print(ch4.get_positions())

# Calculate bond lengths
bond_lengths = []
for i in range(len(ch4.get_positions())):
    for j in range(i + 1, len(ch4.get_positions())):
        distance = np.linalg.norm(ch4.get_positions()[i] - ch4.get_positions()[j])
        if distance > 0:
            bond_lengths.append(distance)

print("\nBond Lengths:")
print(bond_lengths)

# Print the chemical formula
symbols = [atom.symbol for atom in ch4]
print("\nChemical Formula:")
print("".join(symbols))

# Write the molecule to a file (optional)
write("ch4.xyz", ch4)

# Visualize the molecule (optional)
# view(ch4)
