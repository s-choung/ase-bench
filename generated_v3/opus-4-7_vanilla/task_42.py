from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect
import os

dbfile = "metals.db"
if os.path.exists(dbfile):
    os.remove(dbfile)

db = connect(dbfile)

for sym in ["Cu", "Ag", "Au"]:
    atoms = bulk(sym, "fcc")
    atoms.calc = EMT()
    e = atoms.get_potential_energy()
    db.write(atoms, energy=e, name=sym)

for row in db.select():
    print(f"{row.formula}: {row.energy:.6f} eV")
