from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('bulks.db')

for symbol in ['Cu', 'Ag', 'Au']:
    atoms = bulk(symbol, 'fcc')
    atoms.calc = EMT()
    atoms.get_potential_energy()
    db.write(atoms)

for row in db.select():
    print(f"{row.formula}: {row.energy:.4f} eV")
