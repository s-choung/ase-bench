from ase.db import connect
from ase.build import bulk
from ase.calculators.emt import EMT

with connect('bulks.db') as db:
    for sym in ['Cu', 'Ag', 'Au']:
        atoms = bulk(sym)
        atoms.calc = EMT()
        atoms.get_potential_energy()
        db.write(atoms, formula=atoms.get_chemical_formula())

for row in db.select():
    print(row.formula, row.energy)
