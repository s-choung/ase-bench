from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('cu_slabs.db')

for n in [2, 3, 4]:
    atoms = fcc111('Cu', size=(1, 1, n), vacuum=10.0)
    atoms.calc = EMT()
    db.write(atoms, layers=n)

for row in db.select(layers=3):
    print(len(row.toatoms()))
