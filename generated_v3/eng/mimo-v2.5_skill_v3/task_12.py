from ase.build import bulk

ti = bulk('Ti', 'hcp', a=2.95, c=2.95 * 1.59)
print("Cell vectors:")
print(ti.get_cell())
print("\nAtomic positions:")
print(ti.get_positions())
print("\nSymbols:", ti.get_chemical_symbols())
