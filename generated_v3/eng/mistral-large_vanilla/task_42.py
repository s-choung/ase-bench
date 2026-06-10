from ase import Atoms
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('metals.db')

for symbol in ['Cu', 'Ag', 'Au']:
    bulk = Atoms(symbol, cell=[4, 4, 4], pbc=True)
    bulk.calc = EMT()
    energy = bulk.get_potential_energy()
    db.write(bulk, formula=symbol, energy=energy)

for row in db.select():
    print(row.formula, row.energy)
