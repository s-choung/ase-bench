from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect
db = connect('metals.db', append=False)
for s in ['Cu','Ag','Au']:
    a = bulk(s, 'fcc', a=4.0)
    a.calc = EMT()
    a.get_potential_energy()
    db.write(a)
for r in db.select():
    print(r.formula, r.energy)
