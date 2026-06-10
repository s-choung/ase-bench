from ase.build import molecule

ch4 = molecule('CH4')

print(f"Chemical Formula: {ch4.get_chemical_formula()}")
print("\nAtomic Coordinates:")
for atom in ch4:
    print(f"  {atom.symbol}: {atom.position}")

print("\nBond Lengths:")
for i in range(1, len(ch4)):
    d = ch4.get_distance(0, i)
    print(f"  C(0)-H({i}): {d:.4f} Å")
