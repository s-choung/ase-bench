```python
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('cu_slabs.db')
for n in (2, 3, 4):
    slab = fcc111('Cu', size=(2, 2, n), vacuum=10.0, a=3.6)  # 2×2 surface, n layers
    slab.calc = EMT()                                        # optional calculator
    db.write(slab, layers=n)                                 # store with metadata

row = db.select(layers=3).first()        # retrieve the
