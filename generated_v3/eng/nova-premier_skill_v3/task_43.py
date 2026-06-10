from ase import db
from ase.build import fcc111

con = db.connect('cu_slabs.db')  # Connection established
for n in [2, 3, 4]:
    slab = fcc111('Cu', size=(2,2,n), vacuum=10.0)
    con.write(slab, key_value_pairs={'layers': n})

slabs = con.select(layers=3)
print(sum(len(slab) for slab in slabs))  # Total atoms with layers=3
