from ase.db import connect

db = connect('g2.db')
row = next(db.select("name=CH4"), None)
if row:
    atoms = row.toatoms()
    print("Atomic coordinates:\n", atoms.positions)
    print("Chemical formula:", atoms.get_chemical_formula())
    print("C-H bond lengths:", [atoms.get_distance(0, i) for i in range(1, 5)])
else:
    print("CH4 not found in G2 database.")
