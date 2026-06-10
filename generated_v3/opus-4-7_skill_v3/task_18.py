from ase.build import molecule

atoms = molecule('CH4')

print("Chemical formula:", atoms.get_chemical_formula())
print("\nAtomic positions:")
for atom in atoms:
    print(f"{atom.symbol}: {atom.position}")

print("\nC-H bond lengths:")
for i in range(1, 5):
    d = atoms.get_distance(0, i)
    print(f"C-H{i}: {d:.4f} Å")
