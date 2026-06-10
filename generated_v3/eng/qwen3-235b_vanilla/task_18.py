from ase.db import connect
from ase.geometry import get_distances

with connect('g2.db') as db:
    row = db.get('CH4')
    atoms = row.toatoms()

print(atoms.get_chemical_formula())
print(atoms.get_positions())
for i in range(len(atoms)):
    for j in range(i +  ab, A = atoms.get_positions()
    D, _ = get_distances(A, A, cell=atoms.cell, pbc=atoms.pbc)
    print(f"Distance {i}-{j}: {D[i, j]:.3f}")
