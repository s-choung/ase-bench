from ase.build import bulk
from ase.calculators.emt import EMT
import ase.db

db = ase.db.connect('metals.db')
for el in ['Cu', 'Ag', 'Au']:
    atoms = bulk(el)
    atoms.calc = EMT()
    db.write(atoms, energy=atoms.get_potential_energy())
for row in db.select():
    print(row.formula, row.energy)
