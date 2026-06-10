from ase import units
from ase.build import molecule
from ase.geometry import get_distances

# Retrieve CH4 molecule from G2 database
ch4 = molecule('CH4')

# Print atomic coordinates
print("Atomic coordinates (Å):")
for atom in ch4:
    print(f"{atom.symbol:2s}: {atom.position}")

# Calculate and print bond lengths
c_index = 0  # Carbon atom index
h_indices = [i for i, a in enumerate(ch4) if a.symbol == 'H']
dists = get_distances(ch4.positions[c_index:c_index+1], ch4.positions[h_indices])[1]
print("\nC-H bond lengths (Å):")
for i, d in enumerate(dists):
    print(f"  Bond C-H{i+1}: {d:.3f}")

# Print chemical formula
print(f"\nChemical formula: {ch4.get_chemical_formula()}")
