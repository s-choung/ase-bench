from ase.build import molecule

atoms = molecule('CH4')

print("Atomic coordinates (Å):")
for symbol, pos in zip(atoms.get_chemical_symbols(), atoms.get_positions()):
    print(f"  {symbol:2s} {pos[0]:10.6f} {pos[1]:10.6f} {pos[2]:10.6f}")

print(f"\nChemical formula: {atoms.get_chemical_formula()}")

print("\nBond lengths (Å):")
for i in range(1, len(atoms)):
    print(f"  C-{atoms[i].symbol}: {atoms.get_distance(0, i):.4f}")
