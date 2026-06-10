from ase import Atoms
from ase.build import fcc111
from ase.db import connect
from ase.calculators.emt import EMT

# Create database and store Cu slabs with different layer counts
db = connect('cu_slabs.db')
for n_layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, n_layers), vacuum=10.0)
    slab.calc = EMT()
    db.write(slab, layers=n_layers)

# Retrieve structure with layers=3 and print its number of atoms
atoms = db.get_atoms(layers=3)
print(len(atoms))
