from ase.build import fcc111, molecule, add_adsorbate
from ase import Atoms

# Create Al(111) 3-layer slab
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# Get N2 molecule
n2 = molecule('N2')

# Rotate N2 to lie flat (parallel to surface)
n2.rotate(90, 'x', center='COP')

# Find bridge site: midpoint between two adjacent surface atoms
# Top layer atoms indices (last 4 atoms in 2x2x3 slab)
top_layer_indices = [i for i, atom in enumerate(slab) if atom.tag == 2]
# Take first two adjacent atoms in top layer
pos1 = slab.positions[top_layer_indices[0]]
pos2 = slab.positions[top_layer_indices[1]]
bridge_site = (pos1 + pos2) / 2
bridge_site[2] += 2.0  # 2.0 Å above surface

# Add N2 at bridge site
add_adsorbate(slab, n2, height=0.0, position=bridge_site[:2])

# Print info
print(f"Number of atoms: {len(slab)}")
print(f"Atom types: {sorted(set(slab.get_chemical_symbols()))}")
