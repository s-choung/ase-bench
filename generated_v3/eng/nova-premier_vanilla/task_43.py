from ase import db
from ase.build import fcc111

bulk = db.connect('cu_slabs.db')
for n in [2, 3, 4]:
    atoms = fcc111('Cu', size=(1, 1, n), vacuum=10.0)
    bulk.write(atoms, key_value_pairs={'layers': n})

row = bulk.select(layers=3)[0]
print("Atoms in 3-layer slab:", row.toatoms().get_number_of_atoms())
bulk.close()
