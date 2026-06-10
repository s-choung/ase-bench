from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('metals.db')

for symbol in ['Cu', 'Ag', 'Au']:
    atoms = bulk(symbol)
    atoms.calc = EMT()
    db.write(atoms)

for row in db.select():
    print(f"{row.formula}: {row.energy:.4f} eV")
