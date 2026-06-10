from ase import Atoms
from ase.build import fcc111
from ase.db import connect

db = connect('cu_slabs.db')

layers_counts = [2, 3, 4]

for n in layers_counts:
    slab = fcc111('Cu', size=(2, 2, n), vacuum=10.0)
    slab.calc = EMT()
    db.write(slab, layers=n)

retrieved_slab = db.select(rows='layers=3')
if retrieved_slab:
    print(len(retrieved_slab[0]))
