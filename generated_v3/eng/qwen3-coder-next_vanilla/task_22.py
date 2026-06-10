from ase import Atoms
from ase.build import fcc111, molecule
from ase.calculators.emt import EMT

# Create Al(111) 3-layer slab with 4x4 supercell and 10 Å vacuum
slab = fcc111('Al', size=(4, 4, 3), vacuum=10)

# Create N2 molecule
n2 = molecule('N2')
n2.set_distance(1.10)  # Set N≡N bond length to ~1.10 Å

# Place N2 at bridge site (center of 4 Al atoms) at height 2.0 Å above surface
# Get bridge site position (average of 4 Al atoms in top layer)
top_layer_indices = [i for i, atom in enumerate(slab) if atom.z == max([a.z for a in slab])]
bridge_coords = slab[top_layer_indices[:4]].get_center_of_mass()
bridge_coords[2] += 2.0  # Height 2.0 Å above surface
n2.set_positions(n2.get_positions() - n2.get_center_of_mass() + bridge_coords)

# Combine slab and N2
slab_n2 = slab.copy()
slab_n2.extend(n2)

# Print number of atoms and types
print(f"Total atoms: {len(slab_n2)}")
print(f"Atom types: {slab_n2.get_chemical_symbols()}")
