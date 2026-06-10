from ase import Atoms
from ase.build import molecule
from ase.visualize import view
from ase.io import write

# Retrieve the CH4 molecule from the G2 database
ch4 = molecule('CH4')

# Print the atomic coordinates
print("Atomic Coordinates:")
for atom in ch4:
    print(f"  {atom.symbol}: ({atom.position[0]:.4f}, {atom.position[1]:.4f}, {atom.position[2]:.4f})")

# Print the bond lengths
print("\nBond Lengths:")
for i in range(len(ch4)):
    for j in range(i + 1, len(ch4)):
        distance = ((ch4[i].position - ch4[j].position)**2).sum()**0.5
        print(f"  Bond between {ch4[i].symbol} and {ch4[j].symbol}: {distance:.4f}")

# Print the chemical formula
print("\nChemical Formula:", ch4.formula)

# Write the structure to a file (optional)
write('ch4.xyz', ch4)
