from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.db import connect

# Create database connection
db_file = 'cu_slabs.db'
with connect(db_file) as db:
    # Clear existing data if any
    db.purge()

    # Define layer counts to simulate
    layer_counts = [2, 3, 4]

    for n in layer_counts:
        # Create Cu (111) slab
        slab = fcc111('Cu', size=(3, 3, n), vacuum=10.0)
        slab.calc = EMT()
        
        # Store in database with metadata
        db.write(slab, data={'layers': n})

    # Retrieve structure where layers=3
    # select() returns a generator of rows
    target_row = next(db.select(layers=3))
    
    # Print number of atoms
    print(f"Atoms in 3-layer slab: {len(target_row.atoms)}")
