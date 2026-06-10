import os
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db_file = 'metals.db'
if os.path.exists(db_file):
    os.remove(db_file)

db = connect(db_file)

for symbol in ['Cu', 'Ag', 'Au']:
    atoms = bulk(symbol, 'fcc', cubic=True)
    atoms.calc = EMT()
    db.write(atoms, metal=symbol)

print(f"--- Contents of {db_file} ---")
for row in db.select():
    print(f"ID {row.id}: Formula={row.formula}, Energy={row.energy:.4f} eV")
