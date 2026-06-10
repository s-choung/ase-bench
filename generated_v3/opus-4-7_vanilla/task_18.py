from ase.collections import g2

mol = g2['CH4']
print("Formula:", mol.get_chemical_formula())
print("Positions:")
for atom in mol:
    print(f"  {atom.symbol}: {atom.position}")

print("Bond lengths:")
for i in range(len(mol)):
    for j in range(i+1, len(mol)):
        d = mol.get_distance(i, j)
        print(f"  {mol[i].symbol}{i}-{mol[j].symbol}{j}: {d:.4f} Å")
