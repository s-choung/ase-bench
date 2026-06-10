from ase.build import molecule

ch4 = molecule('CH4')
print("Formula:", ch4.get_chemical_formula())
print("Coordinates:")
for sym, pos in zip(ch4.get_chemical_symbols(), ch4.get_positions()):
    print(f"{sym} {pos}")
print("C-H bonds:")
for i in range(1, 5):
    print(f"C-H {i}: {ch4.get_distance(0, i):.4f} Å")
