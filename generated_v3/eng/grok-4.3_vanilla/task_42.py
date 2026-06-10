from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect
db = connect('metals.db')
for s in ['Cu','Ag','Au']:
    a = bulk(s)
    a.calc = EMT()
    a.get_potential_energy()
    db.write(a)
for r in db.select():
    print(r.formula, r.energy)
