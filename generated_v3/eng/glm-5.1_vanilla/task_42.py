from ase.db import connect
from ase.build import bulk
from ase.calculators.emt import EMT

db = connect('metals.db')

for sym in ['Cu', 'Ag', 'Au']:
    atoms = bulk(sym)
    atoms.calc = EMT()
    atoms.get_potential_energy()
    db.write(atoms)

for row in db.select():
    print(f"{row.formula}: {row.energy}")
