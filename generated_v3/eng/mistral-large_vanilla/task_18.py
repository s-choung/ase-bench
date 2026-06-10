from ase.collections import g2
from ase.geometry import bond_length

mol = g2['CH4']
print("Chemical formula:", mol.get_chemical_formula())
print("\nAtomic coordinates (Å):")
for atom in mol:
    print(f"{atom.symbol:2} {atom.position}")
print("\nBond lengths (Å):")
for i, j in [(0, 1), (0, 2), (0, 3), (0, 4)]:
    print(f"C-{mol[j].symbol} {bond_length(mol.positions, i, j):.3f}")
