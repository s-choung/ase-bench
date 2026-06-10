from ase.db import connect
from ase.build import bulk

# Create database and store entries
db = connect('metals.db')

for symbol in ['Cu', 'Ag', 'Au']:
    atoms = bulk(symbol)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, formula=symbol, energy=energy)

# Query and print results
for entry in db.select():
    print(entry.formula, entry.energy)
