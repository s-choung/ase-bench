from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('metals.db')
for symbol, a in [('Cu', 3.615), ('Ag', 4.085), ('Au', 4.078)]:
    atoms = bulk(symbol, 'fcc', a=a)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, energy=energy)

for row in db.select():
    print(row.formula, row.energy)
