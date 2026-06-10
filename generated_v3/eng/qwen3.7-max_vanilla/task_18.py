from ase.build import molecule

ch4 = molecule('CH4')

print("Chemical Formula:", ch4.get_chemical_formula())
print("\nAtomic Coordinates:\n", ch4.positions)

c_idx = ch4.symbols.index('C')
h_idxs = [i for i, s in enumerate(ch4.symbols) if s == 'H']

print("\nC-H Bond Lengths:\n", ch4.get_distances(c_idx, h_idxs))
