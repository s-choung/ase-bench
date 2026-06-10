from ase.db import Database
from ase import Atoms

db = Database('g2.db')
mols = db.get_entries handle

for entry in mols:
    if entry['name'] == 'CH4':
        mol = entry.toatoms()
        break

coords = mol.get_positions()
formula = mol.get_chemical_formula()
bond_lengths = mol.get_distances()

print("Atomic Coordinates:")
print(coords)
print("
Bond Lengths:")
print(bond_lengths)
print("
Chemical Formula:")
print(formula)
