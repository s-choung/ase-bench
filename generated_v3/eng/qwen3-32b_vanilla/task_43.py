import ase.db as db
from ase.build import fcc_slab

conn = db.connect('cu_slabs.db')
for lay in [2, 3, 4]:
    slab = fcc_slab('Cu', size=(4, 4, lay), vacuum=10)
    conn.write(slab, layers=lay)
print(len(next(conn.select('layers=3')).toatoms()))
