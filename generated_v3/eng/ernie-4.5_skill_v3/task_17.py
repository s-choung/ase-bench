from ase import Atoms
from ase.build import surface, bulk
from ase.io import write

# Create Cu fcc bulk
atoms = bulk('Cu', 'fcc', a=3.61)

# Create (2,1,1) surface with 3 layers
slab = surface(atoms, indices=(2,1,1), layers=3, vacuum=10.0)

# Print number of atoms and cell
print(f"Number of atoms: {len(slab)}")
print(f"Cell parameters: {slab.get_cell_lengths_and_angles()}")

# Optional: Write to file
write('Cu_211_slab.xyz', slab)
