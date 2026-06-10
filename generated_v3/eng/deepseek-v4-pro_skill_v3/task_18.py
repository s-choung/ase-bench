from ase.build import molecule

atoms = molecule('CH4')

print("Atomic coordinates:")
for atom in atoms:
    print(f"  {atom.symbol:2} {atom.position}")

print("\nBond lengths:")
for i in range(1, 5):
    print(f"  C-H{i}  {atoms.get_distance(0, i):.4f} Å")

print(f"\nChemical formula: {atoms.get_chemical_formula()}")
