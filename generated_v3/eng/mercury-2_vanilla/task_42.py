from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('metals.db')
calc = EMT()

for elem in ('Cu', 'Ag', 'Au'):
    atoms = bulk(elem, 'fcc')
    atoms.calc = calc
    energy = atoms.get_potential_energy()
    db.write(atoms, energy=energy)

for row in db.select():
    print(row.formula, row.energy)
