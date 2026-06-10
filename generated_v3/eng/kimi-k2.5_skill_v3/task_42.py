from ase.db import connect
from ase.build import bulk
from ase.calculators.emt import EMT

db = connect('metals.db')
for symbol in ['Cu', 'Ag', 'Au']:
    atoms = bulk(symbol, 'fcc', cubic=True)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, energy=energy)

for row in db.select():
    print(row.formula, row.energy)
