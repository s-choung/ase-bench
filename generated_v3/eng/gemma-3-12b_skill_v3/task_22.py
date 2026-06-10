from ase.build import fcc111
from ase.build import molecule
from ase.math import get_distance
from ase.constraints import FixAtoms

slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)
n2 = molecule('N2')

# Find the bridge sites
bridge_sites = []
for x in [-0.5, 0.5]:
    for y in [-0.5, 0.5]:
        bridge_sites.append((x, y))

# Adsorb N2 on the bridge site
adsorb_site = bridge_sites[0]
n2.translate(adsorb_site)
n2.translate([0, 0, 2.0])

# Add the adsorbate to the slab
add_adsorbate = lambda s, a, h, p: s + a
slab += n2  # Directly add n2 to slab

# Fix the slab atoms
slab.set_constraint(FixAtoms(mask=[atom.tag < len(slab) - len(n2) for atom in slab]))

print(f"Number of atoms: {len(slab)}")
print(f"Atom types: {[atom.symbol for atom in slab]}")
