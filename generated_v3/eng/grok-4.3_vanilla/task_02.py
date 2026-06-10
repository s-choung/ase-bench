from ase.build import fcc111, molecule, add_adsorbate
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)
add_adsorbate(slab, molecule('CO'), 1.6, 'ontop')
print(len(slab))
