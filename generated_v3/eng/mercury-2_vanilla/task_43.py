from ase.build import fcc111
from ase.db import connect
from ase.calculators.emt import EMT

db = connect('cu_slabs.db')
for n in (2, 3, 4):
    slab = fcc111('Cu', size=(2, 2, n), vacuum=10.0)
    slab.set_calculator(EMT())
    slab.get_potential_energy()          # run a quick EMT calculation
    db.write(slab, layers=n)             # store with layer count metadata

atoms = list(db.select(layers=3))[0].toatoms()
print(len(atoms))
