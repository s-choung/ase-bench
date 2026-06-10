from ase import Atoms
from ase.build import fcc111
from ase.db import connect

# Connect to ASE database
db = connect('cu_slab.db')

# Store Cu slab structures with different layer counts
layers = [2, 3, 4]
for layer_count in layers:
    atoms = fcc111('Cu', size=(2, 2, layer_count), vacuum=10.0)
    db.write(atoms, layers=layer_count)

# Retrieve structure with layers=3 using select() and print number of atoms
row = db.select(layers=3).next()
print("Number of atoms in the structure with 3 layers:", len(row))  # Number of atoms
