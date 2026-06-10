from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import AtomsWithId

db = AtomsWithId('emt_energies.db')

cu = bulk('Cu', 'fcc', a=3.61)
ag = bulk('Ag', 'fcc', a=4.09)
au = bulk('Au', 'fcc', a=4.07)

calc = EMT()

cu.calc = calc
cu.id = 'Cu_bulk'
db.add_atoms(cu)

ag.calc = calc
ag.id = 'Ag_bulk'
db.add_atoms(ag)

au.calc = calc
au.id = 'Au_bulk'
db.add_atoms(au)

for row in db.select():
    print(f"Formula: {row.formula}, Energy: {row.energy}")
