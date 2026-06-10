from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('metals.db')

for symbol in ['Cu', 'Ag', 'Au']:
    atoms = bulk(symbol, 'fcc', a=4.0)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, data={'energy': energy})

for row in db.select():
    print(f"{row.formula}: {row.data.energy:.4f} eV")
