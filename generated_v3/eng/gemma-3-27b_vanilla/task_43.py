from ase.build import fcc111
from ase.db import AtomsDB
from ase.calculators.emt import EMT

db = AtomsDB('Cu_slabs.db')

layers = [2, 3, 4]
for n in layers:
    slab = fcc111('Cu', size=(n, 4, 3), vacuum=10.0)
    slab.set_calculator(EMT())
    slab.info['layers'] = n
    db.add_atoms(slab)

structures = db.select(filter={'layers': 3})
if structures:
    structure = structures[0]
    print(len(structure))
