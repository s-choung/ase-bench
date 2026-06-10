from ase.db import connect
from ase.build import bulk
from ase.calculators.emt import EMT

db = connect('metals.db')
calc = EMT()

for symbol in ['Cu', 'Ag', 'Au']:
    atoms = bulk(symbol, 'fcc')
    atoms.calc = calc
    energy = atoms.get_potential_energy()
    db.write(atoms, energy=energy)

for row in db.select():
    print(f'{row.formula}: {row.energy:.4f} eV')
