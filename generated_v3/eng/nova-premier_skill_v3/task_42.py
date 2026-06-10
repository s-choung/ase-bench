from ase.db import connect
from ase.build import bulk
from ase.calculators.emt import EMT

db = connect('metals.db')
metals = ['Cu','Ag','Au']

for metal in metals:
    atoms = bulk(metal, cubic=True); atoms.calc = EMT()
    db.write(atoms, metal=metal, energy=float(atoms.get_potential_energy()))

for row in db.select():
    print(f"{row.metal}: {row.energy:.3f} eV")

db.close()
