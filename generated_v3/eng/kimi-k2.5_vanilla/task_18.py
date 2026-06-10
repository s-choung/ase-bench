from ase.build import molecule

atoms = molecule('CH4')
print(f"Formula: {atoms.get_chemical_formula()}")
print("Coordinates:\n", atoms.positions)

c_idx = [i for i, s in enumerate(atoms.symbols) if s == 'C'][0]
for i, s in enumerate(atoms.symbols):
    if s == 'H':
        print(f"C-H distance: {atoms.get_distance(c_idx, i):.3f} Å")
