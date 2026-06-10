from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('metals.db')

for sym, a in [('Cu', 3.6), ('Ag', 4.09), ('Au', 4.08)]:
    atoms = bulk(sym, 'fcc', a=a)
    atoms.calc = EMT()
    atoms.get_potential_energy()
    db.write(atoms)

for row in db.select():
    print(f"{row.formula}: {row.energy:.4f} eV")
