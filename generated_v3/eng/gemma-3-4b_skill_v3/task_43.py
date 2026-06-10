import numpy as np
from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.db import connect
from ase.visualize import view

# Create Cu slab with different layer counts
slab_2 = fcc111('Cu', size=(2, 2, 2), vacuum=10.0)
slab_3 = fcc111('Cu', size=(3, 3, 3), vacuum=10.0)
slab_4 = fcc111('Cu', size=(4, 4, 4), vacuum=10.0)

# Create ASE database
db = connect('cu_slab.db')

# Store structures in the database
db.write(slab_2, key=2)
db.write(slab_3, key=3)
db.write(slab_4, key=4)

# Select structure with layers=3
selected_structure = db.select('layers == 3')

# Print the number of atoms in the selected structure
print(f"Number of atoms in the structure with layers=3: {len(selected_structure)}")

# Optional: Visualize the selected structure
# view(selected_structure)
# db.close()
