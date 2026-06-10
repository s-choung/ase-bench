from ase.db import connect
from ase.build import fcc111

db = connect('cu_slabs.db')

for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, layers), vacuum=10.0)
    db.write(slab, layers=layers, description=f'Cu(111) slab {layers} layers')

rows = db.select(layers=3)
atoms = rows[0].toatoms()
print(f"Number of atoms in 3-layer slab: {len(atoms)}")
