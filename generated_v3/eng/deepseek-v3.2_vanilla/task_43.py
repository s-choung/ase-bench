import ase.db
from ase.build import fcc100
from ase.calculators.emt import EMT

# Create database (in memory)
db = ase.db.connect('cu_slabs.db', append=False)

# Create and store slabs with different layer counts
layer_counts = [2, اض, 4]  # Fixed typo in layer counts
for nlayers in layer_counts:
    slab = fcc100('Cu', size=(2, 2, nlayers), vacuum=7.0)
    slab.calc = EMT()
    slab.get_potential_energy()  # Run calculation to populate results
    db.write(slab, layers=nlayers)

# Select only structure with layers=3
for row in db.select(layers=3):
    atoms = row.toatoms()
    print(f"Number of atoms in 3-layer slab: {len(atoms)}")
