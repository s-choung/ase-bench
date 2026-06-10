from ase.collections import g2

atoms = g2['CH4']

print("Chemical formula:", atoms.get_chemical_formula())
print(f"\nAtomic coordinates (Å):")
for symbol, pos in zip(atoms.get_chemical_symbols(), atoms.positions):
    print(f"  {symbol}: {pos[0]:.4f}  {pos[1]:.4f}  {pos[2]:.4f}")

print(f"\nBond lengths (Å):")
c_idx = atoms.get_chemical_symbols().index('C')
for i, sym in enumerate(atoms.get_chemical_symbols()):
    if sym == 'H':
        d = atoms.get_distance(c_idx, i)
        print(f"  C-H{i}: {d:.4f}")
