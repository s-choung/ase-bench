from ase.build import bulk
from ase.db import connect
from ase.calculators.emt import EMT
import os

db_name = 'metals_emt.db'

if os.path.exists(db_name):
    os.remove(db_name)

db = connect(db_name)

# Cu bulk
cu = bulk('Cu', 'fcc', a=3.61)
cu.calc = EMT()
cu.get_potential_energy()
db.write(cu)

# Ag bulk
ag = bulk('Ag', 'fcc', a=4.09)
ag.calc = EMT()
ag.get_potential_energy()
db.write(ag)

# Au bulk
au = bulk('Au', 'fcc', a=4.08)
au.calc = EMT()
au.get_potential_energy()
db.write(au)

print("Stored structures and energies:")
for row in db.select():
    print(f"Formula: {row.formula}, Energy: {row.energy:.4f} eV")
