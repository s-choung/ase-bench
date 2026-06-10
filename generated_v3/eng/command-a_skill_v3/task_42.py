from ase.db import connect
from ase.build import bulk
from ase.calculators.emt import EMT

# Create database and store structures
db = connect('metals.db', use_lock_file=False)
for symbol in ['Cu', 'Ag', 'Au']:
    atoms = bulk(symbol, 'fcc', a=4.0)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, symbol=symbol, energy=energy)

# Query and print entries
for row in db.select():
    print(f"{row.symbol}: {row.formula}  E={row.energy:.4f} eV")
