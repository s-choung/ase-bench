from ase.build import fcc111, molecule, add_adsorbate

# Generate 3-layer Al(111) slab with 10 Å vacuum
slab = fcc111('Al', size=(3, 3, 3), vacuum=10.0)
# Create isolated N2 molecule
n2 = molecule('N2')
# Place N2 on Al(111) bridge site, 2.0 Å above the surface
add_adsorbate(slab, n2, height=2.0, position=(slab.cell[0,0]/2, 0))

# Print requested structure details
print(f"Total number of atoms: {len(slab)}")
print(f"Unique atom types: {sorted(set(atom.symbol for atom in slab))}")
