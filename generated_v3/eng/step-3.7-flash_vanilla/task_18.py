from ase.g2 import get_molecule

ch4 = get_molecule('CH4')
syms = ch4.get_chemical_symbols()
c_idx = next(i for i, s in enumerate(syms) if s == 'C')
h_idxs = [i for i, s in enumerate(syms) if s == 'H']

print("Atomic coordinates:")
for atom in ch4:
    print(f"{atom.symbol} {atom.x:.3f} {atom.y:.3f} {atom.z:.3f}")

print("\nC-H bond lengths (Å):")
for h in h_idxs:
    print(f"{ch4.get_distance(c_idx, h):.3f}")

formula = ''.join(s + (str(syms.count(s)) if syms.count(s) > 1 else '') 
                 for s in sorted(set(syms), key=lambda x: (0 if x == 'C' else 1 if x == 'H' else 2, x)))
print(f"\nChemical formula: {formula}")
