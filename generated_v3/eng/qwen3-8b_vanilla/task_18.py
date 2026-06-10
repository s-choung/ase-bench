import ase.db
import numpy as np

conn = ase.db.connect('g2.db')
for row in conn.select(formula='CH4'):
    mol = row.toatoms()
    break

print(f"Chemical formula: {mol.get_chemical_formula()}")
print("Atomic coordinates:")
for i in range(len(mol)):
    print(f"{mol[i].symbol} {mol.positions[i]}")
carbon_pos = mol.positions[0]
bond_lengths = [np.linalg.norm(carbon_pos - mol.positions[i]) for i in range(1, 5)]
print("Bond lengths (C-H):", bond_lengths)
