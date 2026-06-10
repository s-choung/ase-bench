from ase.build import fcc111, molecule, add_adsorbate

# Create Al(111) slab: 3 layers, 2x2 surface cell, 10 Å vacuum
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# Build N2 molecule
n2 = molecule('N2')

# Adsorb N2 on a bridge site at height 2.0 Å (approx. position (0.5,0.0) in surface cell)
add_adsorbate(slab, n2, height=2.0, position=(0.5, 0.0))

# Output results
print("Number of atoms:", len(slab))
print("Atom types:", set(slab.get_chemical_symbols()))
