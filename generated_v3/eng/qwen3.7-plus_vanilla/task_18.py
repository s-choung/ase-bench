from ase.data.g2 import g2

mol = g2['CH4']

print(f"Chemical formula: {mol.get_chemical_formula()}")

print("Atomic coordinates:")
for sym, pos in zip(mol.symbols, mol.get_positions()):
    print(f"  {sym}: {pos}")

print("Bond lengths:")
for i, sym_i in enumerate(mol.symbols):
    for j, sym_j in enumerate(mol.symbols[i+1:], start=i+1):
        d = mol.get_distance(i, j)
        if d < 1.5:
            print(f"  {sym_i}-{sym_j}: {d:.4f} A")
