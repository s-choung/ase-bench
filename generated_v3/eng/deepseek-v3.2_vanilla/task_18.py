from ase.collections import g2

# Retrieve CH4 molecule from G2 database
ch4 = g2['CH4']

print("Atomic coordinates:")
for atom in ch4:
    print(f"{atom.symbol:2s} {atom.position[0]:10.6f} {atom.position[1]:10.6f} {atom.position[2]:10.6f}")

print("\nBond lengths:")
c_pos = ch4[0].position
for i in range(1, len(ch4)):
    bond_length = ch4.get_distance(0, i)
    print(f"C-H{i}: {bond_length:.6f} Å")

print(f"\nChemical formula: {ch4.get_chemical_formula()}")
