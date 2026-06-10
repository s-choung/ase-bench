from ase.build import molecule

ch4 = molecule('CH4')

print("Chemical Formula:", ch4.get_chemical_formula())

print("\nAtomic Coordinates (Å):")
for atom in ch4:
    print(f"{atom.symbol:2s} {atom.position[0]:8.4f} {atom.position[1]:8.4f} {atom.position[2]:8.4f}")

print("\nC-H Bond Lengths (Å):")
bond_lengths = ch4.get_distances(0, range(1, len(ch4)))
for i, length in enumerate(bond_lengths):
    print(f"C-H{i+1}: {length:.4f}")
