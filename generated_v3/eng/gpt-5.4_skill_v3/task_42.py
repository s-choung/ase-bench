from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('metals.db')

for metal in ['Cu', 'Ag', 'Au']:
    atoms = bulk(metal, 'fcc', cubic=True)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, metal=metal, energy=energy)

for row in db.select():
    print(row.formula, row.energy)
