from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('metals.db')

for sym in ['Cu', 'Ag', 'Au']:
    atoms = bulk(sym)
    atoms.calc = EMT()
    e = atoms.get_potential_energy()
    db.write(atoms, formula=atoms.get_chemical_formula(), energy=e)

for row in db.select():
    print(row.formula, row.energy)
