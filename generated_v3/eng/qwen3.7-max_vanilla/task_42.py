import os
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db_name = 'noble_metals.db'
if os.path.exists(db_name):
    os.remove(db_name)

db = connect(db_name)

for symbol in ['Cu', 'Ag', 'Au']:
    atoms = bulk(symbol, 'fcc')
    atoms.calc = EMT()
    atoms.get_potential_energy()
    db.write(atoms)

for row in db.select():
    print(f"{row.formula}: {row.energy:.4f} eV")
