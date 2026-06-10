from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('metals.db')
symbols = ['Cu', 'Ag', 'Au']

for symbol in symbols:
    atoms = bulk(symbol, 'fcc')
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, energy=energy)

for row in db.select():
    print(row.formula, row.energy)
