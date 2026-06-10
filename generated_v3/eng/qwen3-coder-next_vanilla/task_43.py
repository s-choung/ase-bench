from ase import Atoms
from ase.build import fcc111
from ase.db import connect
import numpy as np

# Create database
db = connect('cu_slabs.db')

# Cu lattice constant
a = 3.61  # Angstrom

# Generate slabs with 2, 3, and 4 layers
for layers in [2, 3, 4]:
    # Create fcc(111) slab with 3x3 surface unit cell and vacuum
    slab = fcc111('Cu', size=(3, 3, layers), vacuum=10.0, periodic=True)
    
    # Store in database with layers metadata
    db.write(slab, layers=layers)

# Retrieve slab with layers=3
slab_3 = db.get(layers=3)

# Print number of atoms
print(len(slab_3))
