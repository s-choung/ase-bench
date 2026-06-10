from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('metals.db')
for symbol in ['Cu', 'Ag', 'Au']:
    atoms = bulk(symbol, 'fcc', a=3.6)
    atoms.calc = EMT()
    e = atoms.get_potential_energy()
    db.write(atoms, symbol=symbol, energy=e)

for row in db.select():
    print(f"{row.formula:4s} {row.energy:.2f} eV")
db.close()
