from ase.build import bulk
from ase.calculators.emt import EMT
import ase.db

db = ase.db.connect('metals.db')
metals = ['Cu', 'Ag', 'Au']
for symbol in metals:
    atoms = bulk(symbol, 'fcc')
    atoms.calc = EMT()
    db.write(atoms, energy=atoms.get_potential_energy())
for row in db.select():
    print(f"{row.formula}: {row.energy:.4f}")
