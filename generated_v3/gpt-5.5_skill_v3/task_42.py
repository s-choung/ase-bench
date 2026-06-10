from pathlib import Path
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

dbfile = "cu_ag_au_emt.db"
Path(dbfile).unlink(missing_ok=True)

db = connect(dbfile)

for symbol, a in [("Cu", 3.60), ("Ag", 4.09), ("Au", 4.08)]:
    atoms = bulk(symbol, "fcc", a=a)
    atoms.calc = EMT()
    atoms.get_potential_energy()
    db.write(atoms, metal=symbol)

for row in db.select():
    print(row.formula, row.energy)
