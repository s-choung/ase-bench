from ase.collections import g2
from ase.geometry.analysis import Analysis

mol = g2['CH4']

print("Chemical Formula:", mol.get_chemical_formula())
print("\nAtomic Positions:")
for atom in mol:
    print(f"  {atom.symbol}: ({atom.position[0]:.4f}, {atom.position[1]:.4f}, {atom.position[2]:.4f})")

ana = Analysis(mol)
bonds = ana.get_bonds('C', 'H', unique=True)

print("\nC-H Bond Lengths:")
if bonds[0]:
    for bond in bonds[0]:
        i, j = bond
        length = mol.get_distance(i, j)
        print(f"  C({i})-H({j}): {length:.4f} Å")
