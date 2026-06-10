from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

# Create database
db = connect('metals.db')

metals = ['Cu', 'Ag', 'Au']
for m in metals:
    atoms = bulk(m, 'fcc', a=3.6, cubic=True)
    atoms.calc = EMT()
    e = atoms.get_potential_energy()
    db.write(atoms, energy=e)

# Query and print
for row in db.select():
    print(row.formula, row.energy)
