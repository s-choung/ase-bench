from ase.collections import g2
from ase.geometry import get_distances

# Retrieve CH4 molecule from G2 database
ch4 = g2['CH4']

# Print atomic coordinates
print("Atomic coordinates (Å):")
for atom in ch4:
    print(f"{atom.symbol}: {atom.position}")

# Calculate and print bond lengths
positions = ch4.get_positions()
C_index = [i for i, atom in enumerate(ch4) if atom.symbol == 'C'][0]
H_indices = [i for i, atom in enumerate(ch4) if atom.symbol == 'H']
C_H_distances = get_distances(positions[C_index:C_index+1], positions[H_indices], cell=ch4.get_cell(), pbc=ch4.get_pbc())[0]
print(f"\nC-H bond lengths (Å): {C_H_distances.mean():.4f} (average)")

# Print chemical formula
print(f"\nChemical formula: {ch4.get_chemical_formula()}")
