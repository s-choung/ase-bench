from ase.build import bulk
from ase.db import connect
from ase.calculators.emt import EMT

db = connect('metals.db')
calc = EMT()

for metal in ['Cu', 'Ag', 'Au']:
    at = bulk(metal, cubic=True)
    at.calc = calc
    e = at.get_potential_energy()
    db.write(at, formula=at.get_chemical_formula(), energy=e)

for row in db.select():
    print(row.formula, row.energy)
