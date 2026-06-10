from ase import Atoms
from ase.calculators.emt import EMT
from ase.db import connect
from ase.build import bulk

db = connect('bulk_metals.db')

Cu = bulk('Cu', 'fcc', a=3.61)
Cu.calc = EMT()
Cu_energy = Cu.get_potential_energy()
db.write(Cu, formula='Cu', energy=Cu_energy)

Ag = bulk('Ag', 'fcc', a=4.08)
Ag.calc = EMT()
Ag_energy = Ag.get_potential_energy()
db.write(Ag, formula='Ag', energy=Ag_energy)

Au = bulk('Au', 'fcc', a=4.07)
Au.calc = EMT()
Au_energy = Au.get_potential_energy()
db.write(Au, formula='Au', energy=Au_energy)

rows = db.select()
for row in rows:
    print(f"Formula: {row.formula}, Energy: {row.energy} eV")
