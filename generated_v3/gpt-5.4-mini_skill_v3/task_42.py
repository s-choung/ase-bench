from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('metals.db')

for sym in ['Cu', 'Ag', 'Au']:
    atoms = bulk(sym, 'fcc', a=4.0)
    atoms.calc = EMT()
    db.write(atoms, formula=atoms.get_chemical_formula(), energy=atoms.get_potential_energy())

for row in db.select():
    print(row.formula, row.energy)
