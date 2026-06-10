import os
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

dbfile = "metals.db"
if os.path.exists(dbfile):
    os.remove(dbfile)

with connect(dbfile) as db:
    for symbol in ["Cu", "Ag", "Au"]:
        atoms = bulk(symbol, "fcc")
        atoms.calc = EMT()
        atoms.get_potential_energy()
        db.write(atoms, metal=symbol)

    for row in db.select():
        print(row.formula, row.energy)
