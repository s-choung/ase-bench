from ase import Atoms
from ase.db import connect
from ase.calculators.emt import EMT

Cu = Atoms('Cu', [[0, 0, 0]], cell='fcc', pbc=True)
Ag = Atoms('Ag', [[0, 0, 0]], cell='fcc', pbc=True)
Au = Atoms('Au', [[0, 0, 0]], cell='fcc', pbc=True)

Cu.calc = EMT(); Ag.calc = EMT(); Au.calc = EMT()

with connect('bulk.db') as db:
    db.write(Cu, formula='Cu', energy=Cu.get_potential_energy())
    db.write(Ag, formula='Ag', energy=Ag.get_potential_energy())
    db.write(Au, formula='Au', energy=Au.get_potential_energy())

with connect('bulk.db') as db:
    for row in db.select():
        print(row.toatoms().get_chemical_formula(), row.energy)
