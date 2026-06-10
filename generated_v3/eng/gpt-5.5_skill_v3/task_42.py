from pathlib import Path
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

dbfile = "metals.db"
Path(dbfile).unlink(missing_ok=True)

db = connect(dbfile)

for symbol in ["Cu", "Ag", "Au"]:
    atoms = bulk(symbol, "fcc", cubic=True)
    atoms.calc = EMT()
    atoms.get_potential_energy()
    db.write(atoms, metal=symbol)

for row in db.select():
    print(row.formula, row.energy)
