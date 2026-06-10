from ase.db import connect
from ase.build import fcc111
from ase import Atoms
from ase.calculators.emt import EMT

# Create database
db = connect('cu_slab.db')

# Ground‑state slab (no adsorbate)
slab0 = bulk('Cu', 'fcc', a=3.607)  # bulk lattice constant (Fischer et al.)
slab0 = fcc111(slab0, size=(2, 2, 1))

# Add slabs with different layer counts
layers = [2, 3, 4]
for n in layers:
    slab = fcc111(slab0, size=(2, 2, n))
    slab.cell = slab0.cell[:3] + slab.xyz[:, 2] - slab0.xyz[:, 2]  # keep a,b,c from bulk, adjust height
    slab = slab.center()                    # move center to origin
    slab.calc = EMT()
    db.write(slab, layers=n)                # store number of layers as a key
    print(f'Added slab with {n} layers – {slab.get_number_of_atoms()} atoms')

# Retrieve slab with 3 layers and print total atom count
entry = db.select(layers=3)[0]
atoms = entry.toatoms()
print(f'Number of atoms in the 3‑layer Cu slab: {atoms.get_number_of_atoms()}')
