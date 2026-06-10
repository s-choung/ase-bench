from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect("metals.db", append=False)

for sym in ["Cu", "Ag", "Au"]:
    atoms = bulk(sym, "fcc")
    atoms.calc = EMT()
    atoms.get_potential_energy()
    db.write(atoms)

for row in db.select():
    print(row.formula, row.energy)
