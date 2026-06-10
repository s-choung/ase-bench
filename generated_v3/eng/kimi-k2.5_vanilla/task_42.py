from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('metals.db')

for symbol in ['Cu', 'Ag', 'Au']:
    atoms = bulk(symbol)
    atoms.calc = EMT()
    db.write(atoms, energy=atoms.get_potential_energy())

for row in db.select():
    print(row.formula, row.energy)
