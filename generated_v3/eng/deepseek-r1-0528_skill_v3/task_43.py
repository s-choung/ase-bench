from ase.db import connect
from ase.build import fcc111

db = connect(':memory:')  # In-memory SQLite database

for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(1, 1, layers), vacuum=10.0)
    db.write(slab, layers=layers)

result = next(db.select(layers=3))  # Retrieve single entry with layers=3
atoms = result.toatoms()
print(len(atoms))
