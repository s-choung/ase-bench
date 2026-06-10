from ase import build
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('metals.db')

for symbol in ['Cu', 'Ag', 'Au']:
    atoms = build.bulk(symbol, crystalstructure='fcc')
    atoms.set_calculator(EMT())
    energy = atoms.get_potential_energy()
    atoms.info['energy'] = energy
    db.write(atoms)

for entry in db.select():
    print(entry.formula, entry.info['energy'])
